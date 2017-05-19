PyCon 2017
==========

Web and Networking
---------------------

* Python Requests (Cory)
  - Balancing and reacting to concerns
  - Adding tests after writing is close to impossible
  - Emergent behaviour becomes the behviour users depend on
  - Fail better


The art of development
-------------------------

* Testing
  - Advanced testing May 19
    - Mutation Testing
      - pip install cosmic-ray
      - checks for a missing test for coverage cases
      - messes with your code to ensure coverage
      - python 3 only
      - very long execution time
      - used for auditing

    - Fuzz testing
      - Trying to catch uncaught exceptions
      - AFL - american fuzzy lop
        - python-afl
        - takes STDIN and creates a set of sample input files
        - import afl
          - while alf.loop() main

    - Property-based testing
      - testing an assertion of a property
      - generate random input that violates these assertions
      - minimize the example to be as simple as possible
      - *hypothesis* library pip install hypothesis
        - @given(s.integers) deocrator


* Debugging
  - debugging with pdb.set_trace()
    - better than logging or print statement for debugging
    - great
      - inspect contents of variables during real-time execution
        - pp = pretty print

      - traverse frames in call stack
        - bt: allows you to backtrace
          - you can see what the context is and what called it

        - u: up one function call
        - down / d: will go down in the context of the line
        - s: step, continue and execute

      - travel through execution
        - n: execute the one line

      - change live code during execution
        - you can change the variable reference
        - you can also import during execution
        - pp dir(now) functions / attributes available

    - gotchas
      - you can't use this when you can't get a prompt (ipdb)
      - 1 or 2 letter shortcuts means that you can't assign variables
        - you can use `!p` when doing debugging to assign to a letter

      - hitting the enter key will re-enter the command
        - useful to keep pressing "n" etc

    - post-mortem debugging
      - when the program crashes
      - import pdb, then import the code
        - then pdb.pm() for postmortem
          - also lets you do the post_mortem(module)

    - breakpoint
      - break 10: puts a breakpoint at line 10
      - break anagrammer:14 will break on a line in a file
      - break points can also be conditional
      - clear 2
        - clears the 2nd break point

      - break (by itself) you will list all

    - test --pdb will drop to pdb when a test fails


* Exception Handling (Amandine Lee)
  - Your exception should be a cihld of exception
  - why
    - something exceptional happened
      - control flow
        - do you need the exception
        - do you need to jump the stack
        - can you avoid

      - unexpected external error
        - problems with callers
        - problem with callees
        - design by contract
          - client and supplier
            - client
            - supplier
            - maintain invarients

      - bugs in the code (internal error)
        - syntax error
        - raise errors early
          - typechecking!
            - pycharm

        - explicit raise
        - don't obscure with try/except
        - communicate context (stacktrace; etc)


Packaging and Deployment
---------------------------

* Let's Encrypt  (Noah Swartz)
  - Multi Platform deployment
    - certbot-auto
      - a python script which will try to download OS deps too

    - pip install peep = a pipstrap which will do a hash-checking version of pip
    - pyinstaller


* Snek in the browser (Kate)
  - Beeware Suite
    - Batavia
      - Converts python bytecode to JS and other functions

    - Toga
      - GUI compiler

    - colosseum
      - CSS / theme compiler

    - Briefcase
      - Deployment Handling for other machines
      - Can deploy to mobile


* 5 places (Andrew Baker)
  - ngrok
  - heroku
  - "serverless" aws lambda
    - on-demand server
    - pip install zappa
      - Zappa will take care of things in a heroku-like interface
      - zappa init
      - needs a *.app file
      - zappa deploy production
      - zips the archive for dependencies

    - PROS
      - spikey traffic
      - small-to-medium loads

    - CONS
      - new technique
      - still assembling best practices
      - can be very tricy to troubleshoot

  - virtual machines
    - google cloud platform
      - virtualenv -p python3

  - Docker
    - $(docker-machine env <machine>)
