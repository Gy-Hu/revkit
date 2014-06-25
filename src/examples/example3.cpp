/* RevKit: A Toolkit for Reversible Circuit Design (www.revkit.org)
 * Copyright (C) 2009-2011  The RevKit Developers <revkit@informatik.uni-bremen.de>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <iterator>   // for std::distance

#include <core/circuit.hpp>
#include <core/gate.hpp>
#include <core/io/read_realization.hpp>

using namespace revkit;

int main( int argc, char ** argv )
{
  circuit circ;
  read_realization( circ, "circuit.real" );

  foreach ( const gate& g, circ )
  {
    unsigned num_controls = std::distance( g.begin_controls(), g.end_controls() );
    std::cout << "Gate has " << num_controls << " controls." << std::endl;
  }

  return 0;
}
