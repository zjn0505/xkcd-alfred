# xkcd-alfred [![Latest xkcd][1]](https://xkcd.com)

[1]: https://img.shields.io/badge/dynamic/json.svg?label=Latest&url=https%3A%2F%2Fxkcd.com%2Finfo.0.json&query=%24.num&colorB=4BC120&logo=data:image/x-icon;base64,AAABAAIAEBAAAAAAAABoBQAAJgAAACAgEAAAAAAA6AIAAI4FAAAoAAAAEAAAACAAAAABAAgAAAAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAAAAJycnABGRkYAenp6AIODgwAkJCQA6+vrAIyMjAAdHR0A29vbAHx8fAAvLy8Ajo6OADg4OAD///8AFhYWAEpKSgB+fn4AsrKyACgoKAAGBgYA+Pj4AKKiogDW1tYAd3d3AICAgAAqKioAiYmJAOjo6AC9vb0AXl5eAPHx8QBnZ2cA+vr6AHBwcADh4eEAgoKCAIuLiwBgYGAA8/PzAJ2dnQBHR0cAe3t7AOPj4wAlJSUAn5+fANPT0wB0dHQAsbGxAFtbWwCPj48AMDAwADk5OQChoaEAdnZ2AH9/fwApKSkAiIiIAJqamgBvb28AeHh4ANfX1wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0zADc7NwAzMwAEBAATNzM8DgAODg4ADg4ADg4ADg48Ig4aKg4DGg4OKTASDQ4OIiIOKggOOAMODi00NDUODiIZIA4AKAAOHgkOAAAOLh08OQ8bDgAOGwUAFQwMFQAjGBgfAA4ADgAcIQACAgAnDiIiDiQsACwkDgEQAAAQAQ4iIg4OFgAWDg4CAAAAAAIOIiIOJAAAACQOLxEODjsvDiIYKxQXDhcUKzYlDg4OJg4iGTs9Dg4OPTsyAAcOIjsOIhkYPA4ODjw2BwAAAAAKDiIYBgALMgsACQ4xAAAxDg4iPA46AAAAOg4ODg4ODg4OPDMYEQwyDBE7Ozs7Ozs7GDMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAACAAAABAAAAAAQAEAAAAAAAAAgAAAAAAAAAAAAAQAAAAAAAAAAAAAADPz88A39/fACAgIAD///8AcHBwAICAgACQkJAAoKCgANfX1wAoKCgAf39/AIiIiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAAREREAARAAEREAAREQAREAERERABERABERABEREAERABEREQAREQAVEUARERABEQwNERDA0REYHRHDEREQAREQAREQAREREAEQAFEREAEREAJREAERERABmAERERABERDCkQwNERETAiAxEREQARERABEAEREREEAABREREAEAEQwAANEADREMANEQwRABAA0QwA0QwADREAERDA0QARABEQAREAEMDRABEMDREAEQwNEAEQwNEMDQAQwNERABEQwNABDA0REMAAAA0REQAREQAQAQAREREAAAAREREAEREMAAAA0RFAAAAAABURABEREMAADRERQAAAAAAVEQAREREQAREREQAAAAAAEREAEREQwAANEREADREQwBERABEQwAAAAA0RAJEREQgREQAREAAREQABEQEREREQEREAEQwRERERANEADREREBERABEAEREREQARAADREQwREQARAREREREQEQAAERCAEREAEQARERERABEAAAAAABERABEAEREREQARDAAAAADREQARDAAREQAA0RDAAAANEREAERAAAAAAARERLAAC0RERABEQwAAAAA0REREREREREQARERDAAA0REREREREREREAERERERERERERERERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Alfred3 workflow for xkcd comics and what if articles

Developed upon [Alfred-Workflow](http://www.deanishe.net/alfred-workflow/), using [xkcd node APIs](https://github.com/zjn0505/Xkcd)

## Usage

- `xkcd` for recent and most liked comics
- `xkcd {query}` to do a search of `query`
- `⌘` to open comics on [explainxkcd.com](https://explainxkcd.com)
- `whatif` for recent and most liked articles
- `whatif {query}` to do a search of `query`
- `⇧` or `⌘`+`Y` to quicklook comics or articles

## Screenshots

**xkcd search**

![xkcd search](https://raw.githubusercontent.com/zjn0505/xkcd-alfred/master/art/screenshot%201.png)

**what if recent and most liked**

![what if recent and most liked](https://raw.githubusercontent.com/zjn0505/xkcd-alfred/master/art/screenshot%202.png)

## Build dependency

To build this workflow, [Alfred-Workflow](https://github.com/deanishe/alfred-workflow/) is used. Current dependency version `1.3.6`
