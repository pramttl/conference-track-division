## Conference-Track division problem

A project that strives to solve the Optimization problem dealing with grouping a given number of workshops **W**,
into fixed number of tracks **T**, while maximizing the interest of attendes **N**

### Data Collection

First the interests or choices of attendes are collected. 
Imagine a GUI with **W** columns People assign a checkmark (*1*) if they want to attend
a talk, else they let the box remain unchecked (*0*),
The response of each attende is stored as a continous binary string in the *sample_data.txt* file.

#### Here is a rough mockup of what the data in the file looks like.

    1 2 . . . . . . . . . . . W
    ============================
    0 1 1 0 1 1 0 1 0 1 0 0 0 0
    1 0 0 0 1 1 0 1 0 1 0 0 0 1
    .
    .
    .
    0 1 1 1 0 0 0 0 1 0 1 0 1 0


Each row maps to a person and contains a binary string.
1 in a cell indicates that the person would like to attend that workshop. (coulumn)


### Using the data to compute efficient track division - In progress.
//TODO
