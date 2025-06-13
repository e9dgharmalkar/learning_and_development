Git Assessment 3
Below is a list of all the Git commands I have learned and used, along with a brief explanation of what each command does.
`git init`
This starts a new Git repository in the current folder. I used it to tell Git to begin tracking changes in my project.
 `git add <filename>`
This stages the file so Git knows to include it in the next commit. I used this to add files like `README.md`, `.gitignore`, and others before saving my changes.
 `git commit -m "message"`
This saves a snapshot of my project at that moment, along with a short message describing what I did.
`git checkout -b <branch-name>`
This creates a new branch and immediately switches to it. I used this to safely work on new ideas (like feature descriptions or experimental changes) without affecting the main version.
 `git checkout <branch-name>`
I used this to switch between different branches, like going back to `main` after working on another feature branch.
 `git branch`
This shows me all the branches in my project and tells me which one I’m currently on.
`git merge <branch-name>`
This brings the changes from another branch into the current one. I used this to combine my work from `experimental` or `feature-description` into `main`.
 `echo "text" >> <filename>`
This isn't a Git command, but I used it to quickly add content to my files like `README.md` or `contributors.md` using the terminal.
 `.gitignore`
This is a special file that tells Git to ignore certain files and folders so they don’t get added to the repository.
---
What I Learned
Through this exercise, I learned how to track my work using Git, switch between branches to experiment safely, and merge updates smoothly. I also practiced fixing issues when I skipped steps or files didn’t show up correctly.
