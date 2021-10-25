# Simplest case: define a package & module that we then monkey patch.

import foo.foo


def monkey_foo():
    print("Hello from monkey-patch!")


def main():
    print(f'Hello from main-01!')

    # From package foo, module foo, call foo()
    foo.foo.foo()

    # monkey-patch foo() with our local version
    foo.foo.foo = monkey_foo

    # Now invoke the patched function
    foo.foo.foo()

    return


if __name__ == '__main__':
    main()
