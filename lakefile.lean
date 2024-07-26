import Lake
open Lake DSL

/- Define the package configuration for the project.
Includes options for Lean's pretty-printer and implicit argument settings. -/
package «Project» where
  leanOptions := #[
    ⟨`pp.unicode.fun, true⟩,      -- Pretty-print `fun a ↦ b`
    ⟨`autoImplicit, false⟩,       -- Disable auto-implicit arguments
    ⟨`relaxedAutoImplicit, false⟩ -- Disable relaxed auto-implicit arguments
  ]

/- Specify external dependencies required for this project. -/
require mathlib from git "https://github.com/leanprover-community/mathlib4.git"
require checkdecls from git "https://github.com/PatrickMassot/checkdecls.git"

/- Conditionally include the `doc-gen4` dependency in development mode.
This dependency is only required when the environment is set to `dev`.
It ensures that doc-gen is built only in development mode, reducing the build burden for other users.
-/
meta if get_config? env = some "dev" then
require «doc-gen4» from git
  "https://github.com/leanprover/doc-gen4" @ "main"

/- Define the default Lean library target for the project.
This can be customized with additional library configuration options.
-/
@[default_target]
lean_lib «Project» where
  -- Add any library configuration options here
