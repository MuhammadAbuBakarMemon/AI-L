

function minimax(node, depth, alpha, beta, maximizingPlayer) is 

    if depth == 0 or node is a terminal node then 
        return static evaluation of node

    if maximizingPlayer then
        maxeva = -infinity 
        for child in node do
            eva = minimax(child, depth - 1, alpha, beta, false)
            maxeva = max(eva, maxeva)
            alpha = max(alpha, maxeva)
            if alpha >= beta then 
                break
        return maxeva 

    else
        mineva = infinity
        for child in node do
            eva = minimax(child, depth - 1, alpha, beta, true)
            mineva = min(eva, mineva)
            beta = min(beta, mineva)
            if alpha >= beta then
                break
        return mineva  

    

    