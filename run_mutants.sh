# Should install GTIMEOUT first
# MacOS: brew install coreutils

# move to the folder
cd mutants

mutant_count=0
{
filelist="filenames.txt"
echo ${filelist}
while read -r mutant;
do
mutant_count=$((mutant_count + 1))
echo ${mutant}
sudo gtimeout 5s python "${mutant}.py" -init 0 0 -goal 4 5 -filename "${mutant}.txt"
# python "${mutant}.py" -init 0 0 -goal 4 5 -filename "${mutant}.txt"
done < "${filelist}" #while read -r mutant
} #&>
