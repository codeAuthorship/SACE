from tree_sitter import Language, Parser

Language.build_library(
  # Store the library in the `build` directory
  'my-languages2.so',

  # Include one or more languages
  [
     'tree-sitter-go',
    'tree-sitter-javascript',
    'tree-sitter-python',
      'tree-sitter-php',
     'tree-sitter-java',
    'tree-sitter-ruby',
    'tree-sitter-c-sharp',
    'tree-sitter-cpp'
  ]
)
