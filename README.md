# Class Indri
Evening Python Fullstack bootcamp.
Oct 17 - Feb 27

![Indri coding with coffee](./assets/coding_indri.png)
> Image generated with Dall-E

Staff:
- Anthony Wallace, Instructor
  - anthony@pdxcodeguild.com
- Christian Alvarado, TA
  - christian.a@pdxcodeguild.com

<hr>

### Rough Timeline
- Weeks 1, 2, 3, 4, 5: Python
- Weeks 6, 7: HTML/CSS/Flask
- Weeks 8, 9, 10, 11: Django
- Weeks 12, 13, 14, 15: Javascript
- Weeks 16, 17, 18: Capstone project

<hr>

### Scheduled Holidays (no class)
- Oct 21 - Instructor Inservice (no class)
- Nov 24 - Thanksgiving Day
- Dec 26 - Christmas Day (Observed)
- Jan 2 - New Years Day (Observed)

<hr>

### Assigned Labs:

<details open>
  <summary>JavaScript</summary>

| Title | Due Date |
| ----- | -------- |
| [Redo](https://python-documenation-site.deno.dev/javascript/labs/javascript-redo) | 20 JAN |

</details>

<details>
  <summary>Django</summary>

| Title | Due Date |
| ----- | -------- |
| [Polls](https://python-documenation-site.deno.dev/django/mob/polls) | 28 DEC |
| [Redo](https://python-documenation-site.deno.dev/django/labs/django-redo) | 30 DEC |
| [Todo List](https://python-documenation-site.deno.dev/django/labs/todo) | 06 JAN |
| [Chirp](https://python-documenation-site.deno.dev/django/labs/chirp) | 13 JAN |

</details>

<details>
  <summary>HTML/CSS/Flask</summary>

| Title | Due Date |
| ----- | -------- |
| [Bio](https://python-documenation-site.deno.dev/htmlcss/labs/bio) | 07 DEC |
| [Company Landing Page](https://python-documenation-site.deno.dev/htmlcss/labs/company) | 10 DEC |
| [Blog](https://python-documenation-site.deno.dev/htmlcss/labs/blog) | 12 DEC |
| [Burrito Order Form](https://python-documenation-site.deno.dev/htmlcss/labs/burrito-order-form) | 20 DEC |
| [Flask Redo](https://python-documenation-site.deno.dev/htmlcss/labs/flask-redo) | 24 DEC |

</details>

<details>
  <summary>Python</summary>

| Title | Due Date |
| ----- | -------- |
| [Unit Converter](https://python-documenation-site.deno.dev/python/labs/unit-converter) | 02 NOV |
| [Blackjack Advice](https://python-documenation-site.deno.dev/python/labs/blackjack-advice) | 03 NOV |
| [Pick6](https://python-documenation-site.deno.dev/python/labs/pick-6) | 08 NOV |
| [Credit Card Validation](https://python-documenation-site.deno.dev/python/mob/credit-card-validation) | 11 NOV |
| [ROT13](https://python-documenation-site.deno.dev/python/labs/rotation-cipher) | 15 NOV |
| [Count Words](https://python-documenation-site.deno.dev/python/labs/count-words) | 17 NOV |
| [ARI](https://python-documenation-site.deno.dev/python/labs/ari) | 23 NOV |
| [ATM](https://python-documenation-site.deno.dev/python/mob/atm) | 28 NOV |
| [Dad Joke API](https://python-documenation-site.deno.dev/python/labs/dad-joke-api) | 30 NOV |
| [Quotes API](https://python-documenation-site.deno.dev/python/labs/quotes-api) | 02 DEC |

</details>

<hr>

## Class Folder Structure
```
class_indri
├── lecture_notes
├── lab_solutions
├── harry
│   ├── python
│   │   ├── notes
│   │   ├── turtle.py
│   │   ├── turtle_v2.py
│   │   └── mad_lib.py
│   ├── html_css
│   ├── django
│   └── javascript
├── ron
│   ├── python
│   ├── html_css
│   ├── django
│   └── javascript
└── hermione
    ├── python
    ├── html_css
    ├── django
    └── javascript
```
<hr>

## Submitting your work

Make sure all labs are located within `class_indri/<YOUR_NAME>`, where `<YOUR_NAME>` is your first name in all lowercase letters.

To emulate a more professional Git workflow, we're going to start creating new branches for each lab starting in the HTML/CSS section.

<h2>Creating a new branch:</h2>
<details>
<summary>Click to expand</summary>

- `git branch` to check that you're on the main branch, use `git checkout main` to go to the main branch if needed.

- `git status` to check if your local main branch is up to date with origin/main on Github.
- `git pull` if needed to pull any recent changes to your local repository

- Create a new branch and switch to it.

  - Option 1:

    - `git branch <YOUR_NAME-SECTION-LAB_NUMBER>`
    - `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`

  - Option 2:

    The `-b` flag can be used after the `checkout` command to combine these two steps:

    `git checkout -b <YOUR_NAME-SECTION-LAB_NUMBER>`

  **e.g.** My branch for the **"Lab 01 - Bio"** in the **HTML/CSS** section would be named: `anthony-htmlcss-lab01`. The name can vary a bit from this example, but please keep the chosen formatting consistent from one lab to another.

- `git add <FILENAME>` to add a specific file or `git add .` to add everything in the current dicrectory
- `git commit -m "your commit message"` to commit your work

- A remote branch will need to be created for each new local branch. Git will usually display the proper command to do this when a new branch is pushed for the first time.

  The command is:

  `git push --set-upstream origin <BRANCH_NAME>`

  **OR**

  `git push -u origin <BRANCH_NAME>`

- After successfully pushing your new branch to Github, you should see the option to create a Pull Request for your branch on the main repo page.

- If you don't see that message, you'll have to navigate to your new remote branch

- Once you've navigated to your individual branch, you'll find the option to create a Pull Request in the "Contribute" dropdown.

- Click the "Open Pull Request" button. Add a comment to your Pull Request like "Submitting Lab 00" and click "Create Pull request"

</details>

## Updating a branch

<details>
<summary>Click to expand</summary>
After a Pull Request is submitted, the code on that branch will be checked.

Necessary corrections or adjustments will be posted as comments on the Pull Request on Github and the Pull Request will be closed. When the corrections are made, submit the Pull Request again for checking.

Corrections will be made only to that particular branch.

- `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`

- Add and commit updated files.

- `git push` to push your changes up to the remote repository on GitHub

- Only one Pull Request is allowed per branch.

  - If a Pull Request is already open for the branch, a message will be added to the current Pull Request for the new commits.
  - If a Pull Request is not already open for the branch a new Pull Request will need to be created.

- Once a lab is complete, its branch will be merged into the `main` branch.
</details>

---
