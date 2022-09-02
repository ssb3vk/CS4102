/**
 * CS4102 Spring 2022 - Unit A Programming 
 *********************************************
 * Collaboration Policy: You are encouraged to collaborate with up to 3 other
 * students, but all work submitted must be your own independently written
 * solution. List the computing ids of all of your collaborators in the
 * comments at the top of each submitted file. Do not share written notes,
 * documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
 * code. Do not seek published or online solutions, including pseudocode, for
 * this assignment. If you use any published or online resources (which may not
 * include solutions) when completing this assignment, be sure to cite them. Do
 * not submit a solution that you are unable to explain orally to a member of
 * the course staff. Any solutions that share similar text/code will be
 * considered in breach of this policy. Please refer to the syllabus for a
 * complete description of the collaboration policy.
 *********************************
 * Your Computing ID: 
 * Collaborators: 
 * Sources: Introduction to Algorithms, Cormen
 **************************************/
#include<string>
#include<vector>
using namespace std;

class ClosestPair {
    public:

        /**
         * This is the method that should set off the computation
         * of closest pair.  It takes as input a vector containing lines of input
         * as strings.  You should parse that input and then call a
         * subroutine that you write to compute the closest pair distances
         * and return those values from this method.
         *
         * @return the distances between the closest pair and second closest pair
         * with closest at position 0 and second at position 1 
         */
        vector<double> compute(vector<string> fileData) {

            vector<double> closest;
            closest.push_back(0.0); // closest pair distance
            closest.push_back(0.1); // second closest pair distance
            return closest;
        }
};

