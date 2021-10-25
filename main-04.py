# What happens if we get a reference to the module before monkey patching?

import foo.foo as f


def monkey_foo():
    print("Hello from monkey-patch!")


def main():
    print(f'Hello from main-02!')

    # From package foo.foo (as "f"), call foo()
    f.foo()

    # Take a local copy.
    my_foo = f.foo
    my_foo()

    # monkey-patch foo() with our local version
    f.foo = monkey_foo

    # Now invoke the patched function
    f.foo()

    # But we also have a reference to the original version.
    my_foo()

    return


if __name__ == '__main__':
    main()
