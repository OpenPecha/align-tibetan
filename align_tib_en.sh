#!/bin/bash
number_of_overlays=6 # the higher the number of overlays, the more precise alignment is going to be, but also slower
deletion=0.06 # higher = less precise
search_buffer_size=50

# Args:
# first parameter is a file in Tibetan unicode
# second parameter is a file with English in plain text.
# third parameter is output path

cp $1 $1.work
cp $2 $2.work
output_dir=${3:-"output"}
mkdir $output_dir

cp $2.work $2.work2

echo '[INFO] Getting Embedding...'
time python get_vectors.py $1.work $number_of_overlays
time python get_vectors.py $2.work $number_of_overlays

rm ladder
echo '[INFO] Running alignment...'
time ./vecalign.py -a $number_of_overlays -d $deletion --search_buffer_size $search_buffer_size --alignment_max_size $number_of_overlays --src $1.work --tgt $2.work \
   --src_embed $1.work_overlay $1.work_vectors.npy  \
   --tgt_embed $2.work_overlay $2.work_vectors.npy >> ladder

rm $1.org
rm $1.train
python ladder2org.py $1.work $2.work ladder >> $1.org
python create_train.py $1.work $2.work ladder >> $1.train
python create_train_clean.py $1.work $2.work ladder >> $1.train_cleaned

# clean up
mv *.txt* $output_dir/
mv $output_dir/requirements.txt ./
rm $output_dir/$1.work
rm $output_dir/$2.work
rm $output_dir/$2.work2
rm $output_dir/$1.work_vectors.npy
rm $output_dir/$2.work_vectors.npy

echo "[OUTPUT] $output_dir/$1.train_cleaned"
