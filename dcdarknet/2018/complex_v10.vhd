library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all; 

entity complex_v10 is
	port (
		Din : in std_logic_vector(31 downto 0);
		Dout : out std_logic_vector(39 downto 0)
	);
end complex_v10;

architecture imp of complex_v10 is
	-- 10 bit constants
	constant x000 : std_logic_vector(9 downto 0) := (others => '0');
	constant x019 : std_logic_vector(9 downto 0) := "00" & X19;
	constant x022 : std_logic_vector(9 downto 0) := "00" & X"22";
	constant x024 : std_logic_vector(9 downto 0) := "00" & X"24";
	constant x03A : std_logic_vector(9 downto 0) := "00" & X"3A";
	constant x066 : std_logic_vector(9 downto 0) := "00" & X"66";
	constant x067 : std_logic_vector(9 downto 0) := "00" & X"67";
	constant x0DE : std_logic_vector(9 downto 0) := "00" & X"DE";
	constant x0FF : std_logic_vector(9 downto 0) := "00" & X"FF";
	constant x111 : std_logic_vector(9 downto 0) := "01" & X"11";
	constant x155 : std_logic_vector(9 downto 0) := "01" & X"55";
	constant x2A5 : std_logic_vector(9 downto 0) := "10" & X"A5";
	constant x2AA : std_logic_vector(9 downto 0) := "10" & X"AA";
	
	-- break 32-bit input Din into bytes and store it in a 10-bit value
	signal Dinb3 : std_logic_vector(9 downto 0);
	signal Dinb2 : std_logic_vector(9 downto 0);
	signal Dinb1 : std_logic_vector(9 downto 0);
	signal Dinb0 : std_logic_vector(9 downto 0);
begin

	-- break them into bytes and extend to 10 bits
	proc0 : process(Din)
	begin
		Dinb3 <= "00" & Din(31 downto 24);
		Dinb2 <= "00" & Din(23 downto 16);
		Dinb1 <= "00" & Din(15 downto 8);
		Dinb0 <= "00" & Din(7 downto 0);
	end process proc0;		
	
	-- Din(31:24) drives Dout(19:10)
	proc1 : process(Dinb3) 
	begin
		case to_integer(unsigned(Dinb3(7 downto 0))) is
			when to_integer(unsigned(00 )) to to_integer(unsigned( 31 )) => Dout(19 downto 10) <= Dinb3 + x03A;
			when to_integer(unsigned(32)) to to_integer(unsigned(42)) => Dout(19 downto 10) <= Dinb3 - x0DE;
			when to_integer(unsigned(43)) to to_integer(unsigned(55)) => Dout(19 downto 10) <= Dinb3 XOR x2A5;
			when to_integer(unsigned(56)) to to_integer(unsigned(96)) => Dout(19 downto 10) <= std_logic_vector(shift_left(unsigned(Dinb3),3));
			when to_integer(unsigned(97)) to to_integer(unsigned(170)) => Dout(19 downto 10) <= std_logic_vector(rotate_left(unsigned(Dinb3),5)); 
			when to_integer(unsigned(171)) to to_integer(unsigned(255)) => Dout(19 downto 10) <= std_logic_vector(shift_right(unsigned(Dinb3),2));
			when others => Dout(19 downto 10) <= x000;
		end case;  
	end process proc1;

	-- Din(23:16) drives Dout(9:0)
	proc2 : process(Dinb2)
	begin			  
		case to_integer(unsigned(Dinb2(7 downto 0))) is
			when to_integer(unsigned(00)) to to_integer(unsigned(16)) => Dout(9 downto 0) <= NOT Dinb2;
			when to_integer(unsigned(17)) to to_integer(unsigned(44)) => Dout(9 downto 0) <= Dinb2 - x111;
			when to_integer(unsigned(45)) to to_integer(unsigned(68)) => Dout(9 downto 0) <= Dinb2 + x066;
			when to_integer(unsigned(69)) to to_integer(unsigned(187)) => Dout(9 downto 0) <= Dinb2 AND x2AA;
			when to_integer(unsigned(188)) to to_integer(unsigned(222)) => Dout(9 downto 0) <= Dinb2(1) & Dinb2(3) & Dinb2(2) & Dinb2(6) & Dinb2(0) & Dinb2(8) & Dinb2(5) & Dinb2(7) & Dinb2(4) & Dinb2(9);
			when to_integer(unsigned(223)) to to_integer(unsigned(255)) => Dout(9 downto 0) <= Dinb2 + x022;
			when others => Dout(9 downto 0) <= x000;
		end case;
	end process proc2;
	
	-- Din(15:8) drives Dout(39:30)
	proc3 : process(Dinb1)
	begin
		case to_integer(unsigned(Dinb1(7 downto 0))) is
			when to_integer(unsigned(X"00")) to to_integer(unsigned(44)) => Dout(39 downto 30) <= NOT(Dinb1(3 downto 0)) & Dinb1(7 downto 4) & Dinb1(9 downto 8);
			when to_integer(unsigned(45)) to to_integer(unsigned(61)) => Dout(39 downto 30) <= Dinb1 + x024;
			when to_integer(unsigned(62)) to to_integer(unsigned(82)) => Dout(39 downto 30) <= Dinb1 + x0ff;
			when to_integer(unsigned(83)) to to_integer(unsigned(115)) => Dout(39 downto 30) <= Dinb1 - x024;
			when to_integer(unsigned(116)) to to_integer(unsigned(204)) => Dout(39 downto 30) <= Dinb1 - x0ff;
			when to_integer(unsigned(205)) to to_integer(unsigned(255)) => Dout(39 downto 30) <= "10" & (Dinb1(7 downto 4) OR X"1") & (Dinb1(3 downto 0) AND X"E");
			when others => Dout(39 downto 30) <= x000;
		end case;
	end process proc3;
	
	-- Din(7:0) drives Dout(29:20)
	proc4 : process(Dinb0)
	begin					  
		case to_integer(unsigned(Dinb0(7 downto 0))) is
			when to_integer(unsigned(X"00")) to to_integer(unsigned(65)) => Dout(29 downto 20) <= std_logic_vector(rotate_right(unsigned(Dinb0),3));
			when to_integer(unsigned(X"42")) to to_integer(unsigned(90)) => Dout(29 downto 20) <= Dinb0(5) & Dinb0(3) & Dinb0(0) & Dinb0(2) & Dinb0(1) & Dinb0(7) & Dinb0(9) & Dinb0(6) & Dinb0(4) & Dinb0(8);
			when to_integer(unsigned(X"5b")) to to_integer(unsigned(134)) => Dout(29 downto 20) <= Dinb0 + x019;
			when to_integer(unsigned(X"87")) to to_integer(unsigned(175)) => Dout(29 downto 20) <= Dinb0 + x067;
			when to_integer(unsigned(X"b0")) to to_integer(unsigned(223)) => Dout(29 downto 20) <= Dinb0 XOR x2AA;
			when to_integer(unsigned(X"e0")) to to_integer(unsigned(255)) => Dout(29 downto 20) <= Dinb0 XOR x155;
			when others => Dout(29 downto 20) <= x000;
		end case;
	end process proc4;
	
end imp;

