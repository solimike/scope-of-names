# Can we access the module using explicit and synonym names?

import foo.foo          # This is necessary to allow both explicit and synonym namespaces to work.
import foo.foo as f


def monkey_foo():
    print("Hello from monkey-patch!")


def main():
    print(f'Hello from main-03!')

    # From package foo.foo (as "f"), call foo()
    f.foo()

    # monkey-patch foo() with our local version
    f.foo = monkey_foo

    # Now invoke the patched function in the module.
    f.foo()

    # But can we still use the explicit package/module name?  From package foo, module foo, call foo()
    # Only if we import foo.foo directly as well as with an "as" clause!
    foo.foo.foo()

    return


if __name__ == '__main__':
    main()
