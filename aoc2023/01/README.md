##How to run the vim version

Copy the following to your system clipboard:
```
:%s/\v^.{-}(\d).*(\d).*$/\1\2/ | :g/[a-z]/s/^.*\(\d\).*$/\1\1/ | :%j | :s/ /+/g | :exe "norm \"acc\<C-R>=\<C-R>a\r\e"

There seems to be some sort of race condition where the part up to the :%j works, and that part plus the individual :%j works, but those two combined end up calling the :g in the wrong order.
```

Open the input in vim.

Type `@+` and press enter. `"+` is the register that stores the system clipboard, so this runs the macro that you copied earlier.
