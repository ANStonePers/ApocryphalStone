site_name: Adam Stone Digital Portfoio

theme: 
  name: material
  custom_dir: overrides
  palette:
    primary: red
    accent: blue
  features:
    - navigation.tabs
    - navigation.indexes
    - content.code.annotate

nav:
    - Home: index.md
    - Test: test.html

markdown_extensions:
  - attr_list
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
plugins:
    - search
    - mermaid2
    - mkdocs-video