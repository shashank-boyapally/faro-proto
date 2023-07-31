# Arcalot Actions

This repository contains [composite actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) and [reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows#creating-a-reusable-workflow) used in Arcalot.

## Composite actions

All code examples need to be adapted to your existing or new workflow file in your `.github/workflows` folder inside the repository where you want the workflow to run.

### KinD

```
⁞

jobs:
  ⁞
    ⁞
    steps:
      - name: Check out code
        uses: actions/checkout@v3
      - name: Create multi-node KinD cluster
        uses: arcalot/actions/kind@main
      ⁞
```

## Reusable workflows
