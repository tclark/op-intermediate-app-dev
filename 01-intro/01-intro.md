
## IN608
## Intermediate Application Development
---

## Session 1: Introduction
Materials for this paper are available at my [GitHub Repository](https://github.com/tclark/op-intermediate-app-dev).  You will need to clone this repository. I will make updates and changes to it during the semester, so be sure to run `git pull` on it regularly.

For right now, lets look at the [Course Directive](https://github.com/tclark/op-intermediate-app-dev/raw/main/course_directive/course_directive.pdf).

### Our objective for the semester
At this point you're generally able to write code that works. This semester we want to take it further and work on writing code that is good. But what does it mean for code to be good? Generally we here about code being extensible or maintainable. A more straightforward way of describing it is that code should be *readable*.   The principal goal of nearly all developments in programming languages is to make code more easily comprehensible to human readers. The fact that this code may also be executed on a computer is basically an amusing side effect.

Of course, we can't expect other programmers to read code that we don't really understand ourselves. If you're like most programmers, at some point you've written some lines of code that you didn't really understand, but you knew that your program didn't work without them. It was basically *magic* So let's just agree that we're not going to do that in this class. Any time you find yourself using code that you don't understand, stop. Do some reading, ask some questions, and figure out what that code does and why you need it.

Even if you do understand your code, that doesn't mean it's readable by others. It needs to be well thought out and organised according to some coherent design. That's a large part of what we will work on this semester. We will look at some design principles for code and apply them to our work in this paper.

### Setting up your computer for this class
We will use the Python programming language for this class. There are a few reasons for this choice.
  - It's well supported on all of the operating systems that people in this class are likely to use.
  - We're emphasising the importance of writing readable code. Python is known for it's readability and the Python community places a lot of value on that quality.
  - The lecturer likes Python.

  You'll need to have the following things on whatever computers you plan to use for work on this paper.

***Python*** (Version 3.7 or newer)

On Windows there are three ways you can install Python.
  1.  Install the Windows Subsystem for Linux, which will let you use the Python tooling available on Linux. This is probably the easiest option.
  2. Install the [Anaconda](https://www.anaconda.com/products/individual) toolkit. Anaconda is primarily intended to provide tools for data science, but it includes an up-to-date version of Python along with some tools that make it easier to use on Windows. This is what is installed on lab computers.
  3. Install the standard Python distribution from the [Python](https://www.python.org/) web site. While this will work, there is generally some extra fiddling to do to get things set up and working well on Windows.

For Mac users the process is a bit simpler. OS X ships with Python installed, but it's a bad idea to use the default system install of Python on a Mac. Apple doesn't always keep it up-to-date, and if you try to update it yourself you may break some OS X features. Instead, use either Homebrew or MacPorts (whichever you prefer) to install a current Python package. Then modify your shell's path settings to be sure this version of Python is invoked in your shell.

Linux users just need to be sure a current Python package is installed using the package manager.

***A text editor***

The choice of text editor is deeply personal and any programmers' editor will work. If you don't have a strong preference, then Visual Studio Code is a good choice. Microsoft has a good Python language plugin available for VS Code as well.

***Git***

We will use Git for managing code. You will also need a GitHub account to access course materials and submit assessments.

---
 ### Programming Activity

  1. Install Python, Git if necessary
  2. Click the GitHub classroom link for the practicals to set up your repo. Follow
     the instructions on the classroom site.
  3. Clone that repo on your machine.
  4. Edit the `README.md` file at the top level of the practicals directory.
  5. Add, commit, and push to your repo. Confirm that the changes appear.
  6. Create a new branch, `01-practical` in your repo.
  7. In the `01-practical` directory, create a file, `hello.py`. In the file put the code 
     `print('Hello, world')`.
  8. Add, commit, and push the new file.
  9. On the GitHub page for your repo, create a pull request for this commit. Identify `tclark` as 
     the reviewer.
  
Since the goal of this activity is to ensure that you can access and submit your labs correctly, it's important that you do this today.
---

### Coding style

Since we're trying to write readbale code, we need to consider the question of coding *style*. Years ago programmers realised that it was useful to conform to a standard style. It made it easier to recognise the meaning of code when reading it. It also made it easier to code accurately when there was an agreed upon what to name things.

Today most programming languages have an accepted style, but the details differ from language to language. Python has perhaps gone the farthest in this sense in that there is a well documented standard style described in the documnet [PEP 8](https://www.python.org/dev/peps/pep-0008/). This document is long and rather dry, so a [more human readable version](https://pep8.org/) is also available. You should look over these documents, but we'll summarise some important points here. Unlike syntax rules, you *can* break style rules, and sometimes it's acceptable if the resulting code is more readable. Generally, however, you should adhere to these rules.

**File names**: Python source file and directory names should be lower case. Seperate words with an underscore if necessary, but generally keep them short.

**Indenting, line length, and black lines**: 
  - Python is unusual in the indenting is significant. It's necessary indeinting be consistent, but style guidlines call for indent to be four spaces. If you prefer to use your tab key for indents, text editors can be set to use four spaces in place of a tab character.
  - Lines should be fewer than 80 characters long.
  - Class definitions should be seperated with two blank lines. Methods shoule be seperated with one. Top level functions (i.e., not within a class) should be seperated with two lines.
  
 **Naming**:
   - Class names should be `CamelCase`.
   - Variables, method names, etc. should be `lower_case`/`snake_case`.
   - Python doesn't have a `constant` declaration, but constants should be in `UPPER_CASE` and variables presented in this way should be regarded as constant. 
   - If a variable name clashes with a reserved word, you may append a trailing underscore, e.g., `class_`.
   - Names with double leading/trailing underscores, such as `__init__` are reserved for special attributes. You should not introduce your own names with such underscores.

**Comments and docstrings**:

Block comments should precede the code they describe and be indented to the same level. The comment text should be in complete sentences.

```
def calibrate(frobnicator, data):
    # Calibrates the frobnicator using the settings in data.
    ... code follows
```

Modules, classes, and public methods should have *docstrings*.

```
class Parrot:
    """Represents various types of parrots that may be purchased in
    a pet store, e.g., a Norwegian Blue.
    """

    def is_alive(self):
        """Returns True if the parrot is alive."""
        return self._alive
```
Note that 
  - Docstrings always use the triple quote notation.
  - There are no blank lines before and after docstrings.
  - The closing quotes for a multiline docstring go on a line by themselves.

In this class, docstrings aren't required for routine weekly homework, but your major assessments must include appropriate docstrings.

There are some other styles rules that we will introduce when we also discuss the relevant code.

Many text editors have plugins of options to flag Python style violations. There are also utilities like [flake8](https://flake8.pycqa.org/en/latest/) that will scan your files for style compliance.

 