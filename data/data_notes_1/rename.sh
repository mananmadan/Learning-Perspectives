count=0
for f in *.txt
do
  echo $f
  sudo mv "$f" "$count.txt"
  count=`expr $count + 1`
done
