echo 123
undock="700 150"
allviews="760 400"
stopship="471 441"
taboregroup="230 310"
tabore="230 130"
tabstation="230 220"
echo 222
targetlist=("100 125" "100 185" "100 235")
echo 333
targetwarp=("330 125" "330 185" "330 235")
targetlock=("330 125" "330 185" "330 235")
targetwork=("430 125" "430 185" "430 235")
targetaccs=("330 235" "330 285" "330 335")
lightdrone="620 565"
laserminer=("670 565" "670 565" "670 565")
menuavatar="45 45"
menucargo="268 143"
cargo_shipore="90 340"
selectallitem="600 550"
moveitemto="80 160"
moveitemtostationcargo="350 150"
closepage="770 22"
walkto="327 278"
click()
{
    input tap $1 $2
    sleep $3
}
doubleclick()
{
    input tap $1 $2 &sleep 0.3& input tap $1 $2
    sleep $3
}
warptotarget()
{
    click ${targetlist[$1]} 2
    click ${targetwarp[$1]} 40
}
warptooregroup()
{
    click $taboregroup 1
    warptotarget $1
}
locktarget()
{
    click ${targetlist[$1]} 2
    doubleclick ${targetlist[$1]} 2
}
worktarget()
{
    click ${targetlist[$1]} 2
    click ${targetwork[$1]} 4
}
walktotarget()
{
    click ${targetlist[$1]} 2
    click ${targetaccs[$1]} 2
}
work3targets()
{
    click $tabore 1
    walktotarget 0
    locktarget 0
    locktarget 1
    locktarget 2
    worktarget 0
    worktarget 1
    worktarget 2
}
mining()
{
    warptooregroup 2
    #click $lightdrone 1
    let count=5
    while [ count -gt 0 ]
    do
        work3targets
        work3targets
        let count=count-1
    done
}
returnstation()
{
    click $tabstation 1
    warptotarget 0
    sleep 20
    click $menuavatar 3
    click $menucargo 5
    click $cargo_shipore 3
    click $selectallitem 3
    click $moveitemto 3
    click $moveitemtostationcargo 15
} 
leavestation()
{
    click $closepage 2
    click $undock 30
}
while [ 1 -eq 1 ]
do
    leavestation
    click $allviews 2
    mining
    mining
    returnstation
done
