# Sublime

Some config setting for sublime text, sublime merge, and some packages.

## General Config

- Sublime will load the `.zprofile`, not `.zshrc`

In `.zprofile`

```bash
export PATH="/opt/homebrew/bin:$PATH"  ## for homebrew
export PATH="/Users/dingyiyi/.gvm/gos/go1.17/bin:$PATH"  ## for gvm
```

## Template

- [Cpp template](src/sublime/CppTemplate.sublime-macro)
- [Go template](src/sublime/GoTemplate.sublime-macro)

## Sublime Project config

```json
{
  "build_systems":
	[
		{
			"name": "Make lint",
			"shell_cmd": "make lint",
			"working_dir": "$project_path",
			"env": {
				"PATH": "/Users/dingyiyi/.gvm/pkgsets/go1.17/global/bin/:$PATH",
			},
		},
		{
			"name": "gofmt",
			"shell_cmd": "gofmt -d -s -w $file",
			"working_dir": "$project_path",
			"env": {
				"PATH": "/Users/dingyiyi/.gvm/gos/go1.17/bin/:$PATH",
			},
		},
	],
}
```

## Sublime Merge

To show command lists, add `"log_commands": false` in preference settings and open log panel (ctrl + `)

```json
[
    {
        "keys": ["super+shift+m"],
        "command": "edit_commit", // edit commit messages
    },
    {
        "keys": ["super+shift+e"],
        "command": "edit_commit_contents",
        "args": {"commit": "$commit"}
    },
]

```



## Sublime Linter

```json
{
    "debug": false,
    "linters":{
        "g++": {
            "executable": "/opt/homebrew/bin/g++-13",
            "args": "-Wall -fsyntax-only -std=c++20",
            "I": [
                "/opt/homebrew/include",  
                "/Users/dingyiyi/.vcpkg/installed/arm64-osx/include",
                "${project_path}/src/include",
            ],
        },
        "eslint": {
            "excludes": [
                "*.sublime-settings",
                "*.sublime-projects",
            ],
        },
        "golangcilint": {
            "env": {
                "PATH": "/Users/dingyiyi/.gvm/gos/go1.17/bin/:$PATH",
                "GO111MODULE": "on",
            },
            "executable": "/Users/dingyiyi/.gvm/pkgsets/go1.17/global/bin/golangci-lint",
            "working_dir": "${project_path}",
            "args": "--fast ./..."
        },
    },
}
```
