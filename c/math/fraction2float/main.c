/* This program calculates a float out of a fraction.
   Copyright (C) 2012 Fabian Nedoluha <finga@onders.org>

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <stdio.h>
#include <stdlib.h>

long double fraction2float(int num, int denum)
{
  long double result;

  result = (float)num/denum;
  return(result);
}

int get_longest(int num, int denum)
{
  int longest,i;

  for(i=1;num>10;i++)
    {
      num=num/10;
    }
  longest = i;
  for(i=1;denum>10;i++)
    {
      denum=denum/10;
    }
  if(longest<i)
    {
      longest = i;
    }
  return(longest);
}

void print_fraction(int num, int denum, int count)
{
  int i;
  
  printf("%i\n", num);
  for(i=1;i<=count;i++)
    {
      printf("-");
    }
  printf("\n%i", denum);
}

void usage(char *program_name)
{
  printf("Usage: %s <numerator> <denominator>\n", program_name);
  exit(1);
}

void main(int argc, char *argv[])
{
  if(argc == 3)
    {
      int num, denum;

      num = atoi(argv[1]);
      denum = atoi(argv[2]);
      print_fraction(num, denum, get_longest(num, denum));
      printf(" = %Lf\n", fraction2float(num, denum));
      exit(0);
    }
  else
    {
      usage(argv[0]);
    }
}
