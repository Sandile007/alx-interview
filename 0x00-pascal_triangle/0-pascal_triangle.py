#!/usr/bin/python3
program PascalTriangle;

uses crt;

function pascal_triangle(n: Integer): array of array of Integer;
var
  triangle: array of array of Integer;
  i, j: Integer;
begin
  SetLength(triangle, n);
  for i := 0 to n - 1 do
  begin
    SetLength(triangle[i], i + 1);
    triangle[i][0] := 1; // First element in each row is 1
    triangle[i][i] := 1; // Last element in each row is 1
    for j := 1 to i - 1 do
    begin
      triangle[i][j] := triangle[i - 1][j - 1] + triangle[i - 1][j]; // Sum of two above
    end;
  end;
  pascal_triangle := triangle; // Return the triangle
end;

procedure print_triangle(triangle: array of array of Integer; n: Integer);
var
  i, j: Integer;
begin
  for i := 0 to n - 1 do
  begin
    Write('[');
    for j := 0 to i do
    begin
      Write(triangle[i][j]);
      if j < i then
        Write(',');
    end;
    WriteLn(']');
  end;
end;

var
  n: Integer;
  triangle: array of array of Integer;
begin
  n := 5; // You can change this to print more rows
  triangle := pascal_triangle(n);
  print_triangle(triangle, n);
  ReadLn; // To pause the output before closing
end.
