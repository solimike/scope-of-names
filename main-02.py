# Now import the module with a synonym to show patching still works.

import foo.foo as f


def monkey_foo():
    print("Hello from monkey-patch!")


def main():
    print(f'Hello from main-02!')

    # From package foo.foo (as "f"), call foo()
    f.foo()

    # monkey-patch foo() with our local version
    f.foo = monkey_foo

    # Now invoke the patched function
    f.foo()

    return


if __name__ == '__main__':
    main()
