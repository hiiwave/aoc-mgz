"""Map."""

import mgz.const


class Map():
    """Map wrapper."""

    def __init__(self, map_id, x, y, instructions):
        """Initialize."""
        self.size_x = x
        self.size_y = y
        self._size = mgz.const.MAP_SIZES[x]
        if map_id in mgz.const.MAP_NAMES:
            self._name = mgz.const.MAP_NAMES[map_id]
        else:
            self._name = 'Unknown'
            line = instructions.split('\n')[2]
            if line.find(':') > 0:
                self._name = line.split(":")[1].strip()
            elif line.find(b'\xa1\x47') > 0:
                self._name = line.split(b'\xa1\x47')[1].strip()
            elif line.find(b"\xa3\xba") > 0:
                self._name = line.split(b'\xa3\xba')[1].strip()
            self._name = self._name.strip()

    def name(self):
        """Get map name."""
        return self._name

    def size(self):
        """Get map size."""
        return self._size

    def __repr__(self):
        """Get printable representation."""
        return self._name
