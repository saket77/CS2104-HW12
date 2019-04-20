# CS2104-HW12
Q.Four people wish to cross a bridge. It is dark, and it is necessary to use a torch when crossing the bridge, but they have only one torch between them. The bridge is narrow, and only two people can be on it at any one time. The four people take different amounts of time to cross the bridge; when two cross together they proceed at the speed of the slowest. The torch must be ferried back and forth across the bridge, so that it is always carried when the bridge is crossed?

Assume that a solution minimizes the total number of crosses. This gives a total of five crosses - three pair crosses and
two solo-crosses. Also, assume we always choose the fastest for the solo-cross. First, we show that if the two slowest persons
(C and D) cross separately, they accumulate a total crossing time of 15. This is done by taking persons 
A, C, & D: C+A+B+A = 8+1+5+1=15. (Here we use A because we know that using A to cross both C and D separately 
is the most efficient.) But, the time has elapsed and person A and B are still on the starting side of the bridge 
and must cross. So it is not possible for the two slowest (C & D) to cross separately. Second, we show that in order 
for C and D to cross together that they need to cross on the second pair-cross: i.e. not C or D, so A and B, must 
cross together first. Remember our assumption at the beginning states that we should minimize crosses and so we have
five crosses - 3 pair-crossings and 2 single crossings. Assume that C and D cross first. But then C or D must cross 
back to bring the torch to the other side, and so whoever solo-crossed must cross again. Hence, they will cross 
separately. Also, it is impossible for them to cross together last, since this implies that one of them must have 
crossed previously, otherwise there would be three persons total on the start side. So, since there are 
only three choices for the pair-crossings and C and D cannot cross first or last, they must cross together
on the second, or middle, pair-crossing. Putting all this together, A and B must cross first, since we 
know C and D cannot and we are minimizing crossings. Then, A must cross next, since we assume we should 
choose the fastest to make the solo-cross. Then we are at the second, or middle, pair-crossing so C and
D must go. Then we choose to send the fastest back, which is B. A and B are now on the start side and 
must cross for the last pair-crossing. This gives us, B+A+D+B+B = 2+1+8+2+2 = 15.
I use two other sums to get the best result
