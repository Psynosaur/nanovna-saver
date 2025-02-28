#! /bin/env python

#  NanoVNASaver - a python program to view and export Touchstone data from a NanoVNA
#  Copyright (C) 2019.  Rune B. Broberg
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyQt5 import QtWidgets

from NanoVNASaver import NanoVNASaver

version = "0.0.4"

if __name__ == '__main__':
    print("NanoVNASaver " + version)
    print("Copyright (C) 2019 Rune B. Broberg")
    print("This program comes with ABSOLUTELY NO WARRANTY")
    print("This program is licensed under the GNU General Public License version 3")
    print("")
    print("See https://github.com/mihtjel/nanovna-saver for further details")
    # Main code goes here
    app = QtWidgets.QApplication([])
    window = NanoVNASaver()
    window.show()
    app.exec_()
