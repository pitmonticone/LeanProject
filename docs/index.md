---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

# layout: home
usemathjax: true
---

# Fermat's Last Theorem for Exponent 3

This project formalises Fermat's Last Theorem for the exponent 3 using the Lean 4 interactive proof assistant.

## Build Lean Files

To build the Lean files of this project, you need to have a working version of Lean.
For comprehensive guidance on installing Lean,
see [the installation instructions](https://leanprover-community.github.io/get_started.html)
under the section titled "Regular install".

To build the project, run `lake exe cache get` and then `lake build`.

## Build Blueprint

To build the web version of the blueprint, you need a working LaTeX installation.
Furthermore, you need some packages:

```
sudo apt install graphviz libgraphviz-dev
pip3 install invoke pandoc
cd .. # go to folder where you are happy clone git repos
git clone git@github.com:plastex/plastex
pip3 install ./plastex
git clone git@github.com:PatrickMassot/leanblueprint
pip3 install ./leanblueprint
cd FLT3
```

To actually build the blueprint, run

```
lake exe cache get
lake build
inv all
```