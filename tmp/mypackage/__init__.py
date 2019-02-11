from . import another

PACKAGE_VERSION = 2.0

bar = 2
baz = bar ** 3 ** bar
bun = bar / another.add(bar, baz)
