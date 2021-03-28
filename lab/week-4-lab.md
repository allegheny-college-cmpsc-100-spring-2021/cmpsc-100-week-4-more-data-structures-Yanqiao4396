### CMPSC 100: G. Wiz and the Ballot Bonanza

![GO VOTE](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-ballot-bonanza.png)

<div class="alert alert-block alert-warning" id = "warning">
The work this week also offers the opportunity to tie up the server in loopish operations. Should you be unable to run cells, key in <B>CTRL + C</b> (<B>⌘ + C</b> for Apple folks -- I call it "flower").</div>

At times in a Gator's life, it's important to consider whether on not to get involved in the political process beyond merely being a voter. Realizing that they might make a very good Pond Representative, G. Wiz recently confronted this democratic _raison d'etre_. In a fiercely fought campaign against several other reptile representative candidates, G. Wiz awaits the election results from a fancy new computerized system which promises extremely fast results. May the...most...voted...for reptile win?

The only problem is that _you_ have to write the machine. 

You've been given some test data, but the real votes will be counted when the `gradle grade` process runs.

## General guidelines for laboratory sessions

---

* Follow steps carefully. Laboratory sessions often get a bit more complicated than their preceeding course sessions. Especially for early sessions which expose you to platforms with which you may not be familiar, take notes on commands you run and their corresponding effects/outputs. If you find yourself stuck on a step, let a TL or the professor know! Laboratory sessions do not mean that we won't guide you in the same way we do during other sessions.
* Regularly ask and answer questions. Some of you may have more experience with the topics we're discussing than others. We can use this knowledge to our advantage. Let students try things for a while before offering help (always offer first). To ask questions, use your group's Slack channel or TL channels.
* Store and transfer files using GitHub. Various forms of file storage are more or less volatile. You are responsible for backing up and storing files. If you're unsure of files which have been changed, you can always type git status in the terminal for your working folder to determine what you need to back up.
* Keep all of your files. See above, but also remember that you're responsible for the files you create.
* Back up your files regularly. See above (and above-above).
* Review the Honor Code regularly when working. If you're taking a solution from another student or the Internet at-large (especially Stack Overflow), bear in mind that using these solutions can constitute a form of plagiarism that violates the Allegheny Honor Code. While it may seem easy and convenient to use these sources, it is equally easy and convenient to rely on them and create bad habits which include not attributing credit or relying exclusively on others to solve issues. Neither are productive uses of your intellect. Really.

## Requirements

---

### Python File

Your program should:

* Create a `dictionary` called `ballot`
* Read the file located at `.inputs/.votes` to collect votes
  * Recall that the `rstrip()` method of `string` will be useful here, just like in the [File I/O worksheet](../worksheets/2_week-4-worksheet-io.ipynb)
* Add one vote to the selected candidate's vote total
* Using a `for` loop, `print`, according to [sample output](#Sample-output) below:
  * vote totals for all candidates
  * the name of the winner
* Use `7` _ORIGINAL_ single-line comments
  
Note: your test data will not be as extensive as the data used by the grader; your work should satisfy both test and grader cases

#### Hint(s)

* Determining the winner may use an `if` statement

### `reflection.md`

* At least 250 words
* Responds to all questions
* Contains `0` `TODO` markers

### Test data

|Candidate | Votes |
|----------|-------|
|G. Wiz    | 6     |
|Frogger   | 3     |
|Slippy Toad | 4   |
|Lyle Crocodile| 5   |
|Yertle Turtle | 2   |

### Sample output

```
Frogger received 3 votes.
.
.
.
.
.
G. Wiz received 6 votes.
The winner is G. Wiz -- with 6 votes.
```

The numbers and order above will change, as the amount of votes contained in the file located at [.inputs/.votes](.inputs/.votes) is much larger.

## Notes

This work should be completed in the [week-4-lab.py](week-4-lab.py) file.

<div class="alert alert-block alert-danger" id = "warning">
    <b>THIS WEEK</b>, of all weeks, will tempt you to program the <i>answer</i> rather than the solution. The grader output contains the correct answers that it expects the program to print. However, remind yourself that the <i>answer</i> is not the <i>solution</i>. The only way to fully solve this one is to code it correctly!
</div>