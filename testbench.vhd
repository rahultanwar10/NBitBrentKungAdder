library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use STD.textio.all;
use ieee.std_logic_textio.all;

entity testbench is end entity;

architecture testbench_arch of testbench is
constant nBit: integer := 32; signal A,B,sum: std_logic_vector(nBit-1 downto 0);
signal Cin, Carry_out:  std_logic; file inputFile, outputFile : text;

begin
dut : entity work.finalAdder(dataflowFinalAdder) 	generic map (nBit=>nBit) 
																	port map(A,B,Cin,Sum,Carry_out);
process
variable n_iline,n_oline: line; variable n_space: character;
variable add_1,add_2,sum_cal,Sum_out: std_logic_vector(nBit-1 downto 0);
variable carry_in,carry_ou,Carry,correct : std_logic;
begin
file_open(inputFile, "C:/Vector/inputVector.txt", read_mode);
file_open(outputFile, "C:/Vector/output.txt", write_mode);
while not (endfile(inputFile)) loop
readline(inputFile, n_iline);
read(n_iline, add_1);
read(n_iline, n_space);
read(n_iline, add_2);
read(n_iline, n_space);
read(n_iline, carry_in);
read(n_iline, n_space);
read(n_iline, sum_cal);
read(n_iline, n_space);
read(n_iline, carry_ou);
A <= add_1;
B <= add_2;
Cin <= carry_in;
wait for 10ns;
Sum_out := Sum;
Carry := Carry_out;
if (Sum_out = sum_cal) and (Carry = carry_ou) then correct := '1'; else correct := '0'; end if;
assert (correct = '1') report "Wrong Calculation" severity FAILURE;
write(n_oline, Sum_out,right,nBit);
write(n_oline, n_space);
write(n_oline, Carry);
write(n_oline, n_space);
write(n_oline, correct);
writeline(outputFile, n_oline); end loop;
file_close(inputFile); file_close(outputFile);
wait; end process; end architecture;