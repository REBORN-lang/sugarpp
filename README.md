# sugar++
**sugar++** (or **sugarpp**) is a tiny transpiler for [Reborn](https://github.com/REBORN-lang)-like syntactic sugar in **C++23**

## Guide
Here you will learn how to create a simple program in the **sugar++** syntax.

### Hello World program
We recommend using the `<print>` header added in the [**ISO C++23 Standard**](https://isocpp.org/std/the-standard) instead of the older `std::cout` object.
```
// hello_world.spp
include print

main: int() {
	std::println("Hello, World!");
	return 0;
}
```
Then, to compile we are gonna need to actually transpile the **s++** code to **C++**. \
To do that we are gonna use the **sugar++** [Python](https://www.python.org/) transpiler which you can find [here](https://github.com/REBORN-lang/sugarpp/blob/main/sugarpp.py) in this repo. \
The syntax is simple: `sugarpp <input_file.spp> <output_file.cpp>` \
And with that we got a standard `.cpp` file we can compile with `g++`, `clang++` or any other **C++** compiler.

### Other examples
You can find other examples in this repo, more specifically, in the `examples/` directory.

# Extras
There is a simple [Neovim](https://neovim.io) syntax highlighting plugin for `.spp` (**sugar++**) files.
-> [Link to guide](https://github.com/REBORN-lang/.github/blob/main/misc/SugarppNeovimThemeGuide.md)

&nbsp;
### Maintainers
- jstmax! : <jstmaxlol@disroot.org> & <maxwasmailed@proton.me>
