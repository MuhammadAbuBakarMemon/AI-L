#pseudocode for MINIMAX ALGORITHM

function(node, depth, maximizingPlayer)

    if (depth == 0 or node is terminal node) then
        return static evaluation of node 
        -- the heuristic function we apply that evaluates how good our board looks, like in a chess game if we have more pieces then our opp then it 
        -- it gives us a +5 rating, if you are loosing then it would return a -3 
        
        -- for maximizer player 
    if maximizingPlayer then
        maxeva = -infinity 
        for each child in node do
            eva = minimax(child, depth - 1, false)
            maxeva = max(maxeva, eva)
        return (maxeva)
    else 
        --  for minimizaer player
        mineva = +infinity
        for each child in node do 
            eva = minimax(child, depth - 1, true)
            mineva = min(eva, mineva)
        return mineva

