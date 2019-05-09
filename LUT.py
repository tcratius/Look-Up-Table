# numpy has an insanely powerful way to create 'dictionaries' from an array (a):

lut, ndx = np.unique(a, return_inverse=True)

# Now you have a list of unique values in (lut) and a list of indices to them in (ndx) ...fast!
# Depending on number of distinct values, index array can be compressed to file by typecasting:

if len(lut) < 256:

ndx = ndx.astype(np.uint8) #byte

b = np.memmap(outFileName, dtype=ndx.dtype, mode='w+', shape=ndx.shape)

b[:] = ndx[:]

# to recreate the original fully specified array (a) after reading from disk:
a = np.array(lut)[ndx]

# If your task is to constantly access a particular column for all rows, this column-based approach 
# beats row-based RDBMSs by miles and miles and miles.
# BTW 'dictionary encoding' effectively also happens in a classic RDBMS when joining a 'fact table' 
# to a 'dimension table' (everybody calls it LUT for 'lookup table' in my experience) .
