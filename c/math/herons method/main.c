/* This program calculates the square root by the babylonian method.
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

long double wurzelvonbabel_quadrat(long double radikant)
{
  long double a[255], wurzel;
  int i;

  a[0] = (radikant+1)/2;
  for(i=0;i<=255;i++)
  {
    printf("Durchlauf: %i\tMittelwert: %.64Lf\n", (i), a[(i)]);
    a[(i+1)] = (a[i]+radikant/a[i])/2;
    if(a[(i+1)]*a[(i+1)] == radikant || a[i] == a[(i+1)])
    {
      wurzel = a[(i+1)];
      i=255;
    }
  }
  return wurzel;
}

void usage(char *program_name)
{
  printf("Usage: %s <radikant>\n", program_name);
  exit(1);
}

int main(int argc, char *argv[])
{
  if(argc == 2)
  {
    long double radikant = strtold(argv[1],0);

    printf("Radikant: %.64Lf\n", radikant);
    printf("Ergebnis: %.64Lf\n", wurzelvonbabel_quadrat(radikant));
  }else{
    usage(argv[0]);
  }
}
