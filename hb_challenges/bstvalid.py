"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False
"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is tree a valid BST?

        This recurses similiarly to `is_valid`, but it uses
        exceptions to immediate exit when an invalid value is
        found. Using execeptions for quick control-passing can
        sometimes make for clearer code.
        """

        def _ok(n, less_than_this, greater_than_this):
            """Check this node & recurse to children."""

            if n is None:
                return

            if ((less_than_this is not None and n.data > less_than_this) or
                    (greater_than_this is not None and n.data < greater_than_this)):
                raise ValueError

            _ok(n.left, n.data, greater_than_this)
            _ok(n.right, less_than_this, n.data)

        try:
            _ok(self, None, None)
            return True

        except ValueError:
            return False


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.")
