
## IN608
## Kaiako: Tom Clark
---

## Session 1: Introduction
Materials for this paper are available at my [GitHub Repository](https://github.com/tclark/op-intermediate-app-dev).  You will need to clone this repository. I will make updates and changes to it during the semester, so be sure to run `git pull` on it regularly.

For right now, lets look at the [Course Directive](https://github.com/tclark/op-intermediate-app-dev/raw/main/course_directive/course_directive.pdf).

### Our objective for the semester
At this point you're generally able to write code that works. This semester we want to take it further and work on writing code that is good. But what does it mean for code to be good? Generally we here about code being extensible or maintainable. A more straightforward way of describing it is that code should be *readable*.   The principal goal of nearly all developments in programming languages is to make code more easily comprehensible to human readers. The fact that this code may also be executed on a computer is basically an amusing side effect.

Of course, we can't expect other programmers to read code that we don't really understand ourselves. If you're like most programmers, at some point you've written some lines of code that you didn't really understand, but you knew that your program didn't work without them. It was basically *magic* So let's just agree that we're not going to do that in this class. Any time you find yourself using code that you don't understand, stop. Do some reading, ask some questions, and figure out what that code does and why you need it.

Even if you do understand your code, that doesn't mean it's readable by others. It needs to be well thought out and organised according to some coherent design. That's something we will work on this semester. We will look at some design principles for code and apply them to our work in this paper.

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





