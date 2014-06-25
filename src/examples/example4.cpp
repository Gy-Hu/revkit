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

#include <boost/assign/std/set.hpp>     // for using += operator with gate::line_container

#include <core/circuit.hpp>
#include <core/functions/add_gates.hpp>

using namespace boost::assign;
using namespace revkit;

int main( int argc, char ** argv )
{
  circuit circ( 5 );

  append_cnot( circ, 2, 3 );
  prepend_v( circ, 0, 1 );
  append_fredkin( circ )( 0, 1 )( 2, 4 );
  insert_vplus( circ, 2, 1, 2 );
  prepend_not( circ, 2 );

  gate::line_container controls;
  controls += 0,1,2,3;
  append_toffoli( circ, controls, 4 );
}
