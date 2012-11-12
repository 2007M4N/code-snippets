/* This program calculates the fibonacci numbers.
   Copyright (C) 2012 Roman Gerhardt <rootman@onders.org>,
   Fabian Nedoluha <finga@onders.org>

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

void f_fibonacci(int v_i)
{
  long long int v_fibonacci[v_i];
  int i;
  v_fibonacci[0]=0;
  v_fibonacci[1]=1;
  for (i=-1;i<v_i;i++)
    {
      v_fibonacci[i+3]=v_fibonacci[i+2]+v_fibonacci[i+1];
      printf("Durchlauf:\t%i\tfibonacci Zahl:\t%lli\n",i+1,v_fibonacci[i+1]);
    }
}

void usage(char *program_name)
{
  printf("Usage: %s <Genauigkeit>\n", program_name);
  exit(1);
}
void main(int argc, char *argv[])
{
  if(argc == 2)
  {
    int fibonacci = atoi(argv[1]);
    f_fibonacci(fibonacci);
  }
  else
  {
    usage(argv[0]);
  }
  
}
