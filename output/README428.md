# Simple Go Assertion Library

This is a very simple library to avoid having to include external dependencies into the Arcaflow codebases.

You can include it in your project by running:

```
go get go.arcalot.io/assert
```

You can then use it like this:

```go
package your_test

import "go.arcalot.io/assert"

func TestSomething(t *testing.T) {
    assert.NotNil(t, nil)
}
```

You can find the detailed documentation at [pkg.go.dev/go.arcalot.io/assert](https://pkg.go.dev/go.arcalot.io/assert).