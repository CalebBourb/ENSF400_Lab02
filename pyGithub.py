from github import Github

# or using an access token
g = Github("")
repo = g.get_repo("CalebBourb/ENSF400_Lab02")

print("Branches")
print("--------------")
branches = repo.get_branches()
for branch in branches:
    print(branch.name)

print()
print("Pull Requests")
print("--------------")
prs = repo.get_pulls(state='all')
for pr in prs:
    print(pr.title + ": " + pr.state)

print()
print("Commits")
print("--------------")
commits = repo.get_commits()
for commit in commits:
    print(commit.commit.author.name + ", " + str(commit.commit.author.date) + "  :  " + commit.commit.message)
