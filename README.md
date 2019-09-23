# batchDownloadFromWeb
# 1.将本地工程推到github上
1.1VCS-> import into version control-> share project on github

1.2更新：VCS->commit, VCS->git->push

# 2.创建branch
2.1 VCS-> git-> branch
在本地创建的branch，更新到github时，也会自动在github上添加一个branch。 然后在branch上做的修改，更新之后，也对是github上对应分支进行更新。

# 3.当master和dev两个branch都发生改变时，此时merge会发生什么
dev为master init的状态下创建的分支。后来master也发生了改变。此时要把他们进行merge操作，就会在pull request页面，给你展示dev跟最新的master的不同，然后人为的来确定，在最新master的基础上，要把dev的哪些改进放进master，得到更新的master版本。

反正在master上进行操作，是实时更新的，branch做修改，最后merge时是要和最新的master进行比较的。

使用思路：比较稳定的版本都放到master上，然后在branch上进行修改。直到branch得到新的稳定版本，再把他推给master进行合并。
