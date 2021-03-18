from flask import Flask,jsonify

app = Flask(__name__)

posts_algo={
    'articles':[
                {
                    'title':'Linear Search',
                    'image':'https://thumbs.dreamstime.com/z/search-icon-vector-ads-collection-thin-line-outline-illustration-linear-symbol-use-web-mobile-apps-logo-print-142852398.jpg',
                    'content':'https://computergeek985841235.wordpress.com/linear-search/',
                    'text':'A simple approach to do linear search is - Start from the leftmost element of arr[] and one by one compare x with each element of arr[], If x matches with an element, return the index. If x doesn’t match with any of elements, return -1.',
                    'Video_1':'https://www.youtube.com/watch?v=4GPdGsB3OSc',
                    'Video_2':'https://www.youtube.com/watch?v=avVXSm3sXaw',
                    'Video_3':'https://www.youtube.com/watch?v=UldZOLylez4&t=17s',
                    'Video_4':'https://www.youtube.com/watch?v=Q-qN0pJWh5s'
                },
                {
                    'title':'Binary Search',
                    'image':'https://i.ytimg.com/vi/OUP-F5Oeng8/maxresdefault.jpg',
                    'content':'https://www.geeksforgeeks.org/binary-search/',
                    'text':'Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.',
                    'Video_1':'https://www.youtube.com/watch?v=P3YID7liBug',
                    'Video_2':'https://www.youtube.com/watch?v=d-nh-xBHsgM&t=4s',
                    'Video_3':'https://www.youtube.com/watch?v=DE-ye0t0oxE',
                    'Video_4':'https://www.youtube.com/watch?v=vohuRrwbTT4'
                },
                {
                    'title':'Selection Sort',
                    'image':'https://images.slideplayer.com/25/7853136/slides/slide_26.jpg',
                    'content':'https://www.geeksforgeeks.org/selection-sort/',
                    'text':'The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.',
                    'Video_1':'https://www.youtube.com/watch?v=Lrd1QaKyok4',
                    'Video_2':'https://www.youtube.com/watch?v=Jb8AYaYMxq4',
                    'Video_3':'https://www.youtube.com/watch?v=gbyJiRiLZ2s',
                    'Video_4':'https://www.youtube.com/watch?v=xWBP4lzkoyM'
                },
                {
                    'title':'Bubble Sort',
                    'image':'https://play-lh.googleusercontent.com/LDEZbpGS__if6k0LPK8AcGk9IuRDIw8mIwMTpQkNIOvv_rCOF1Al5S3WS9A8WJlIkw',
                    'content':'https://www.geeksforgeeks.org/bubble-sort/',
                    'text':'Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.',
                    'Video_1':'https://www.youtube.com/watch?v=re9ytVtt5zg',
                    'Video_2':'https://www.youtube.com/watch?v=BJkpnxf5cfY',
                    'Video_3':'https://www.youtube.com/watch?v=xcPFUCh0jT0',
                    'Video_4':'https://www.youtube.com/watch?v=QD0-eIBbr1w'
                },
                {
                    'title':'Insertion Sort',
                    'image':'https://www.sitesbay.com/data-structure/images/sorting/insertion-sort.png',
                    'content':'https://www.geeksforgeeks.org/insertion-sort/',
                    'text':'Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.',
                    'Video_1':'https://www.youtube.com/watch?v=s9fmGjFY1v0',
                    'Video_2':'https://www.youtube.com/watch?v=3GC83dh4cf0',
                    'Video_3':'https://www.youtube.com/watch?v=8l3dH_XyCik',
                    'Video_4':'https://www.youtube.com/watch?v=OGzPmgsI-pQ'   
                },
                {
                    'title':'Merge Sort',
                    'image':'https://1.bp.blogspot.com/--gk1a9udOaY/XrwOLvZuPQI/AAAAAAAACNw/AeqY3HYeY9MgYdYlu4rgAv_2mUpXEshOwCLcBGAsYHQ/w1200-h630-p-k-no-nu/maxresdefault%2B%25281%2529.jpg',
                    'content':'https://www.geeksforgeeks.org/merge-sort/',
                    'text':'Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.',
                    'Video_1':'https://www.youtube.com/watch?v=6Aqxv29RGPc',
                    'Video_2':'https://www.youtube.com/watch?v=mB5HXBb_HY8',
                    'Video_3':'https://www.youtube.com/watch?v=JSceec-wEyw',
                    'Video_4':'https://www.youtube.com/watch?v=4z9I6ZmeLOQ'
                },
                {
                    'title':'HeapSort',
                    'image':'https://www.edureka.co/blog/wp-content/uploads/2019/07/2-3-300x300.png',
                    'content':'https://www.geeksforgeeks.org/heap-sort/',
                    'text':'Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.',
                    'Video_1':'https://www.youtube.com/watch?v=Q_eia3jC9Ts',
                    'Video_2':'https://www.youtube.com/watch?v=MtQL_ll5KhQ',
                    'Video_3':'https://www.youtube.com/watch?v=HqPJF2L5h9U',
                    'Video_4':'https://www.youtube.com/watch?v=2DmK_H7IdTo'
                },
                {
                    'title':'QuickSort',
                    'image':'https://coderzpy.com/wp-content/uploads/2020/12/Quick-Sort-346x188.png',
                    'content':'https://www.geeksforgeeks.org/quick-sort/',
                    'text':'Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.',
                    'Video_1':'https://www.youtube.com/watch?v=7h1s2SojIRw',
                    'Video_2':'https://www.youtube.com/watch?v=tWCaFVJMUi8',
                    'Video_3':'https://www.youtube.com/watch?v=SN4x87ZdhGg',
                    'Video_4':'https://www.youtube.com/watch?v=PgBzjlCcFvc'
                },
                {
                    'title':'BFS for Graph',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/',
                    'text':'Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this post). The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are reachable from the starting vertex. ',
                    'Video_1':'https://www.youtube.com/watch?v=pcKY4hjDrxk',
                    'Video_2':'https://www.youtube.com/watch?v=0u78hx-66Xk',
                    'Video_3':'https://www.youtube.com/watch?v=YYq38LTz774',
                    'Video_4':'https://www.youtube.com/watch?v=uQtX6dfbk0M'
                },
                {
                    'title':'DFS for Graph',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/',
                    'text':'Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice. To avoid processing a node more than once, use a boolean visited array.',
                    'Video_1':'https://www.youtube.com/watch?v=pcKY4hjDrxk',
                    'Video_2':'https://www.youtube.com/watch?v=Y40bRyPQQr0',
                    'Video_3':'https://www.youtube.com/watch?v=CvUMf8c2JFo',
                    'Video_4':'https://www.youtube.com/watch?v=lo1P6bhsoG4'
                },
                {
                    'title':'Detect Cycle in DAG',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/detect-cycle-in-a-graph/',
                    'text':'Depth First Traversal can be used to detect a cycle in a Graph. DFS for a connected graph produces a tree. There is a cycle in a graph only if there is a back edge present in the graph.',
                    'Video_1':'https://www.youtube.com/watch?v=0dJmTuMrUZM',
                    'Video_2':'https://www.youtube.com/watch?v=joqmqvHC_Bo',
                    'Video_3':'https://www.youtube.com/watch?v=AK7BuT5MgU0',
                    'Video_4':'https://www.youtube.com/watch?v=1u2VLzBhJZU'
                },
                {
                    'title':'Detect Cycle in Undirected Graph',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/detect-cycle-undirected-graph/',
                    'text':'Run a DFS from every unvisited node. Depth First Traversal can be used to detect a cycle in a Graph. DFS for a connected graph produces a tree.',
                    'Video_1':'https://www.youtube.com/watch?v=eCG3T1m7rFY&t=590s',
                    'Video_2':'https://www.youtube.com/watch?v=L0DcePeWHnM',
                    'Video_3':'https://www.youtube.com/watch?v=6ZRhq2oFCuo',
                    'Video_4':'https://www.youtube.com/watch?v=6PSczvPWGak'
                },
                {
                    'title':'Topological Sort',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/topological-sorting/',
                    'text':'Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.',
                    'Video_1':'https://www.youtube.com/watch?v=qe_pQCh09yU',
                    'Video_2':'https://www.youtube.com/watch?v=Q9PIxaNGnig',
                    'Video_3':'https://www.youtube.com/watch?v=7CTpoVNIc8o',
                    'Video_4':'https://www.youtube.com/watch?v=dis_c84ejhQ'
                },
                {
                    'title':'Bipartite Check',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/bipartite-graph/',
                    'text':'A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.',
                    'Video_1':'https://www.youtube.com/watch?v=0ACfAqs8mm0',
                    'Video_2':'https://www.youtube.com/watch?v=MtFPqCcsoeA',
                    'Video_3':'https://www.youtube.com/watch?v=y22G2QXwpiI',
                    'Video_4':'https://www.youtube.com/watch?v=HqlUbSA9cEY'
                },
                {
                    'title':'Dijkstra’s Algo',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/',
                    'text':'Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph. we generate a SPT (shortest path tree) with given source as root. We maintain two sets, one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree.',
                    'Video_1':'https://www.youtube.com/watch?v=XB4MIexjvY0',
                    'Video_2':'https://www.youtube.com/watch?v=Sj5Z-jaE2x0',
                    'Video_3':'https://www.youtube.com/watch?v=d6ZFqjH63vo',
                    'Video_4':'https://www.youtube.com/watch?v=NR4fpjuxnPA'
                },
                {
                    'title':'Bellman–Ford Algorithm',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/',
                    'text':'Dijkstra doesn’t work for Graphs with negative weight edges, Bellman-Ford works for such graphs. Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems. But time complexity of Bellman-Ford is O(VE), which is more than Dijkstra.',
                    'Video_1':'https://www.youtube.com/watch?v=FtN3BYH2Zes',
                    'Video_2':'https://www.youtube.com/watch?v=Sj5Z-jaE2x0',
                    'Video_3':'https://www.youtube.com/watch?v=FrLWd1tJ_Wc',
                    'Video_4':'https://www.youtube.com/watch?v=obWXjtg0L64'
                },
                {
                    'title':'Floyd Warshall Algorithm',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/facebook-graph.png',
                    'content':'https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/',
                    'text':'The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.',
                    'Video_1':'https://www.youtube.com/watch?v=oNI0rf2P9gE',
                    'Video_2':'https://www.youtube.com/watch?v=nV_wOZnhbog',
                    'Video_3':'https://www.youtube.com/watch?v=K6rI0umX-28',
                    'Video_4':'https://www.youtube.com/watch?v=QnUf_AiFgc8'
                },
                {
                    'title':'Exponentiation',
                    'image':'https://hackernoon.com/hn-images/1*z0fUKBPH_qyPQX6F3wuDPQ.png',
                    'content':'https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/',
                    'text':'In mathematics, exponentiation (power) is an arithmetic operation on numbers. It can be thought of as repeated multiplication, just as multiplication can be thought of as repeated addition.',
                    'Video_1':'https://www.youtube.com/watch?v=-3Lt-EwR_Hw',
                    'Video_2':'https://www.youtube.com/watch?v=L-Wzglnm4dM',
                    'Video_3':'https://www.youtube.com/watch?v=8nOaPV-o5Pg',
                    'Video_4':'https://www.youtube.com/watch?v=HN7ey_-A7o4'
                },
                {
                    'title':'Inversions',
                    'image':'https://hackernoon.com/hn-images/1*z0fUKBPH_qyPQX6F3wuDPQ.png',
                    'content':'https://www.geeksforgeeks.org/counting-inversions/',
                    'text':'Inversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order, the inversion count is the maximum.',
                    'Video_1':'https://www.youtube.com/watch?v=owZhw-A0yWE',
                    'Video_2':'https://www.youtube.com/watch?v=k9RQh21KrH8',
                    'Video_3':'https://www.youtube.com/watch?v=sV4RhDIIKO0',
                    'Video_4':'https://www.youtube.com/watch?v=vFH3zrUbvD4'
                }
        ]
    }

posts_ds={
    'articles':[
                {
                    'title':'Array',
                    'image':'https://cdn.programiz.com/sites/tutorial2program/files/c-arrays.jpg',
                    'content':'https://www.geeksforgeeks.org/array-data-structure/',
                    'text':'An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).',
                    'Video_1':'https://www.youtube.com/watch?v=55l-aZ7_F24',
                    'Video_2':'https://www.youtube.com/watch?v=JJ2iSrwIkVs',
                    'Video_3':'https://www.youtube.com/watch?v=NptnmWvkbTw',
                    'Video_4':'https://www.youtube.com/watch?v=lpQ4VCir1IA'
                },
                {
                    'title':'Linked List',
                    'image':'https://res.cloudinary.com/dpessyoae/image/upload/v1494083335/linkedlist3_fsadk8.png',
                    'content':'https://www.geeksforgeeks.org/data-structures/linked-list/',
                    'text':'A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.',
                    'Video_1':'https://www.youtube.com/watch?v=R9PTBwOzceo',
                    'Video_2':'https://www.youtube.com/watch?v=Crqgl10aIGQ',
                    'Video_3':'https://www.youtube.com/watch?v=zjUlSAR9YmY'
                },
                {
                    'title':'Stack',
                    'image':'https://images-platform.99static.com//Xo9a2qEZF4QatvukeNQlMFm9jOk=/396x1119:896x1619/fit-in/590x590/projects-files/45/4541/454183/e8c3703e-383e-4444-b1c7-5dec58965188.png',
                    'content':'https://www.geeksforgeeks.org/stack-data-structure/',
                    'text':'Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).',
                    'Video_1':'https://www.youtube.com/watch?v=-n2rVJE4vto',
                    'Video_2':'https://www.youtube.com/watch?v=JvuaAgDar1c',
                    'Video_3':'https://www.youtube.com/watch?v=r7P9sy5Rar8'
                },
                {
                    'title':'Queue',
                    'image':'https://cdn.dribbble.com/users/523915/screenshots/5744319/queue-logo.png',
                    'content':'https://www.geeksforgeeks.org/queue-data-structure/',
                    'text':'A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.',
                    'Video_1':'https://www.youtube.com/watch?v=UbAEP7P0vfk',
                    'Video_2':'https://www.youtube.com/watch?v=sDO9bPaBg6A',
                    'Video_3':'https://www.youtube.com/watch?v=fbonDkYsKj0'
                },
                {
                    'title':'Binary Tree',
                    'image':'https://i.pinimg.com/originals/c2/6f/9b/c26f9bfdd74a186a8f17926f091c0175.png',
                    'content':'https://www.geeksforgeeks.org/binary-tree-data-structure/',
                    'text':'A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.',
                    'Video_1':'https://www.youtube.com/watch?v=I_JuQ5ayPmc',
                    'Video_2':'https://www.youtube.com/watch?v=j8b4ZnZefBo',
                    'Video_3':'https://www.youtube.com/watch?v=zW4JZt6Wud8'
                },
                {
                    'title':'Binary Search Tree',
                    'image':'https://miro.medium.com/max/664/1*xd2O7AZm_ZVJrS3-0JyDDg.png',
                    'content':'https://www.geeksforgeeks.org/binary-search-tree-data-structure/',
                    'text':'BST is a collection of nodes arranged in a way where they maintain BST properties. Each node has a key and an associated value. While searching, the desired key is compared to the keys in BST and if found, the associated value is retrieved.',
                    'Video_1':'https://www.youtube.com/watch?v=sXABdGalFNg',
                    'Video_2':'https://www.youtube.com/watch?v=XQJJhNiGlL0',
                    'Video_3':'https://www.youtube.com/watch?v=VVXOE-hnFts'
                },
                {
                    'title':'Min Heap',
                    'image':'https://media.geeksforgeeks.org/wp-content/uploads/20201106115157/MinHeap.jpg',
                    'content':'https://www.journaldev.com/36805/min-heap-binary-tree',
                    'text':'A Min Heap Binary Tree is a Binary Tree where the root node has the minimum key in the tree.The above definition holds true for all sub-trees in the tree. This is called the Min Heap property.',
                    'Video_1':'https://www.youtube.com/watch?v=g9YK6sftDi0',
                    'Video_2':'https://www.youtube.com/watch?v=U7iED4L4oy8',
                    'Video_3':'https://www.youtube.com/watch?v=rb_KU0dZy9E'
                },
                {
                    'title':'Max Heap',
                    'image':'https://www.codingninjas.com/blog/wp-content/uploads/2020/12/MaxHeap.png',
                    'content':'https://www.geeksforgeeks.org/max-heap-in-java/',
                    'text':'A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.',
                    'Video_1':'https://www.youtube.com/watch?v=g9YK6sftDi0',
                    'Video_2':'https://www.youtube.com/watch?v=U7iED4L4oy8',
                    'Video_3':'https://www.youtube.com/watch?v=rb_KU0dZy9E'
                },
                {
                    'title':'Hashing',
                    'image':'https://uploads.toptal.io/blog/image/129310/toptal-blog-image-1551794764808-260dc8495f15e76a523f52a512d48acb.png',
                    'content':'https://www.geeksforgeeks.org/hashing-data-structure/',
                    'text':'Hashing is an important Data Structure which is designed to use a special function called the Hash function which is used to map a given value with a particular key for faster access of elements. The efficiency of mapping depends of the efficiency of the hash function used.',
                    'Video_1':'https://www.youtube.com/watch?v=W5q0xgxmRd8',
                    'Video_2':'https://www.youtube.com/watch?v=AV36hu5TFRQ',
                    'Video_3':'https://www.youtube.com/watch?v=wWgIAphfn2U'
                },
                {
                    'title':'Graph',
                    'image':'https://1.bp.blogspot.com/-kzNOIqci3jI/XvA1AjkZj-I/AAAAAAAAgLM/b5M4vCV0cbIxjviKXm247BVYD1P84zfOgCLcBGAsYHQ/s400/Graph%2BData%2BStructure%2Bwith%2Bnodes.png',
                    'content':'https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/',
                    'text':'A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.',
                    'Video_1':'https://www.youtube.com/watch?v=5eKDQmTzX2A',
                    'Video_2':'https://www.youtube.com/watch?v=1n5XPFcvxds',
                    'Video_3':'https://www.youtube.com/watch?v=4xMsNIPEkwA&list=PLFj4kIJmwGu3m30HfYDDufr3PZBfyngr0',
                    'Video_4':'https://www.youtube.com/watch?v=qci480hbh1Q'
                }
        ]
    }

posts_data={
    'articles':[
                {
                    'title':'Data link layer Intro',
                    'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFKgzjqMbwanbdt8lftHdAm-xaXJdFdrsebg&usqp=CAU',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/data_link_layer_introduction.htm',
                    'text':'Data Link Layer is second layer of OSI Layered Model. This layer is one of the most complicated layers and has complex functionalities and liabilities. Data link layer hides the details of underlying hardware and represents itself to upper layer as the medium to communicate.',
                    'Video_1':'https://www.youtube.com/watch?v=JRgmPco0KWI',
                    'Video_2':'https://www.youtube.com/watch?v=VBAuzvVzOQU',
                    'Video_3':'https://www.youtube.com/watch?v=iYdW0B1olLE',
                },
                {
                    'title':'CSMA',
                    'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFKgzjqMbwanbdt8lftHdAm-xaXJdFdrsebg&usqp=CAU',
                    'content':'https://www.geeksforgeeks.org/carrier-sense-multiple-access-csma/',
                    'text':'This method was developed to decrease the chances of collisions when two or more stations start sending their signals over the datalink layer. Carrier Sense multiple access requires that each station first check the state of the medium before sending.',
                    'Video_1':'https://www.youtube.com/watch?v=IftFvfSywCQ',
                    'Video_2':'https://www.youtube.com/watch?v=MAZi6VoekYw',
                    'Video_3':'https://www.youtube.com/watch?v=PyLlYQXuxvs',
                },
                {
                    'title':'CSMA/CD',
                    'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFKgzjqMbwanbdt8lftHdAm-xaXJdFdrsebg&usqp=CAU',
                    'content':'https://www.geeksforgeeks.org/collision-detection-csmacd/',
                    'text':'CSMA/CD (Carrier Sense Multiple Access/ Collision Detection) is a media-access control method that was widely used in Early Ethernet technology/LANs, When there used to be sharedBus Topology and each Nodes( Computers) were connected By Coaxial Cables.Now a Days Ethernet is Full Duplex and CSMA/CD is not used as Topology is either Star (connected via Switch or Router)or Point to Point ( Direct Connection) but they are still supported though.',
                    'Video_1':'https://www.youtube.com/watch?v=v_z888gQWq0',
                    'Video_2':'https://www.youtube.com/watch?v=FzzM84zfNws',
                    'Video_3':'https://www.youtube.com/watch?v=K_8KJRhOWIA',
                },
                {
                    'title':'Error Detection & Correction',
                    'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFKgzjqMbwanbdt8lftHdAm-xaXJdFdrsebg&usqp=CAU',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/error_detection_and_correction.htm',
                    'text':'Data-link layer uses some error control mechanism to ensure that frames (data bit streams) are transmitted with certain level of accuracy. But to understand how errors is controlled, it is essential to know what types of errors may occur.',
                    'Video_1':'https://www.youtube.com/watch?v=U7-h2hyM1Dc',
                    'Video_2':'https://www.youtube.com/watch?v=EMrY-8m8D1E',
                    'Video_3':'https://www.youtube.com/watch?v=IHoHPem6cYE',
                },
                {
                    'title':'Data-link Control & Protocols',
                    'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFKgzjqMbwanbdt8lftHdAm-xaXJdFdrsebg&usqp=CAU',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/data_link_control_and_protocols.htm',
                    'text':'Data-link layer is responsible for implementation of point-to-point flow and error control mechanism.',
                    'Video_1':'https://www.youtube.com/watch?v=yNedVgNyE8Q',
                    'Video_2':'https://www.youtube.com/watch?v=N2tgsPUPEBE',
                    'Video_3':'https://www.youtube.com/watch?v=bhU2nRF36q4',
                }               
        ]
    }

posts_application={
    'articles':[
                {
                    'title':'Application Layer Introduction',
                    'image':'http://www.ibdaahub.com/wp-content/uploads/2017/11/Untitled-6-08-263x263.png',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/application_layer_introduction.htm',
                    'text':'Application layer is the top most layer in OSI and TCP/IP layered model. This layer exists in both layered Models because of its significance, of interacting with user and user applications. This layer is for applications which are involved in communication system.',
                    'Video_1':'https://www.youtube.com/watch?v=8An0dRalJeM',
                    'Video_2':'https://www.youtube.com/watch?v=3s4yWb8izVs',
                    'Video_3':'https://www.youtube.com/watch?v=mGRClHHgNdk',
                },
                {
                    'title':'Client Server Model',
                    'image':'http://www.ibdaahub.com/wp-content/uploads/2017/11/Untitled-6-08-263x263.png',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/application_layer_introduction.htm',
                    'text':'In client-server model, any process can act as Server or Client. It is not the type of machine, size of the machine, or its computing power which makes it server; it is the ability of serving request that makes a machine a server.',
                    'Video_1':'https://www.youtube.com/watch?v=L5BlpPU_muY',
                    'Video_2':'https://www.youtube.com/watch?v=SwLdKeC8scE',
                    'Video_3':'https://www.youtube.com/watch?v=B8azMzrluHE',
                },
                {
                    'title':'Application Protocols',
                    'image':'http://www.ibdaahub.com/wp-content/uploads/2017/11/Untitled-6-08-263x263.png',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/application_protocols.htm',
                    'text':'The Domain Name System (DNS) works on Client Server model. It uses UDP protocol for transport layer communication. DNS uses hierarchical domain based naming scheme. The DNS server is configured with Fully Qualified Domain Names (FQDN) and email addresses mapped with their respective Internet Protocol addresses.',
                    'Video_1':'https://www.youtube.com/watch?v=pnoWCK82apU',
                    'Video_2':'https://www.youtube.com/watch?v=RcKZ2dygroU',
                    'Video_3':'https://www.youtube.com/watch?v=jpOgng-SmEY',
                },
                {
                    'title':'Network Services',
                    'image':'http://www.ibdaahub.com/wp-content/uploads/2017/11/Untitled-6-08-263x263.png',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/network_services.htm',
                    'text':'Computer systems and computerized systems help human beings to work efficiently and explore the unthinkable. When these devices are connected together to form a network, the capabilities are enhanced multiple-times. Some basic services computer network can offer are.',
                    'Video_1':'https://www.youtube.com/watch?v=LYmTUXQy_2U',
                    'Video_2':'https://www.youtube.com/watch?v=oOxKLCkbz-A',
                    'Video_3':'https://www.youtube.com/watch?v=HEz1WYQO8Hs',
                }
        ]
    }

posts_transport={
    'articles':[
                {
                    'title':'Transport Layer Introduction',
                    'image':'https://joinup.ec.europa.eu/sites/default/files/styles/horizontal_medium_image/public/deafult_logo_1_32.png?itok=S6nvcw7y',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/transport_layer_introduction.htm',
                    'text':'Next Layer in OSI Model is recognized as Transport Layer (Layer-4). All modules and procedures pertaining to transportation of data or data stream are categorized into this layer. As all other layers, this layer communicates with its peer Transport layer of the remote host.',
                    'Video_1':'https://www.youtube.com/watch?v=kAty4mKczEg',
                    'Video_2':'https://www.youtube.com/watch?v=CAjdS1Eq6k4',
                    'Video_3':'https://www.youtube.com/watch?v=MmK8Ra8J_1o',
                },
                {
                    'title':'Transmission Control Protocol',
                    'image':'https://joinup.ec.europa.eu/sites/default/files/styles/horizontal_medium_image/public/deafult_logo_1_32.png?itok=S6nvcw7y',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/transmission_control_protocol.htm',
                    'text':'The transmission Control Protocol (TCP) is one of the most important protocols of Internet Protocols suite. It is most widely used protocol for data transmission in communication network such as internet.',
                    'Video_1':'https://www.youtube.com/watch?v=c8aet11HNxg',
                    'Video_2':'https://www.youtube.com/watch?v=5ex1s4lURto',
                    'Video_3':'https://www.youtube.com/watch?v=5Ywo4X0ujaU',
                },
                {
                    'title':'User Datagram Protocol',
                    'image':'https://joinup.ec.europa.eu/sites/default/files/styles/horizontal_medium_image/public/deafult_logo_1_32.png?itok=S6nvcw7y',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/user_datagram_protocol.htm',
                    'text':'The User Datagram Protocol (UDP) is simplest Transport Layer communication protocol available of the TCP/IP protocol suite. It involves minimum amount of communication mechanism. UDP is said to be an unreliable transport protocol but it uses IP services which provides best effort delivery mechanism.',
                    'Video_1':'https://www.youtube.com/watch?v=HF_znV8x9a0',
                    'Video_2':'https://www.youtube.com/watch?v=blV7WUZpkCE',
                    'Video_3':'https://www.youtube.com/watch?v=jJyXpMmXJI0',
                }
        ]
    }


posts_networks={
    'articles':[
                {
                    'title':'Network Layer Introduction',
                    'image':'https://i.pinimg.com/736x/e8/4f/cc/e84fcc53a804c981fff96dfbd9f7a8b7.jpg',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/network_layer_introduction.htm',
                    'text':'Layer-3 in the OSI model is called Network layer. Network layer manages options pertaining to host and network addressing, managing sub-networks, and internetworking.',
                    'Video_1':'https://www.youtube.com/watch?v=mxpoZ56MqoY',
                    'Video_2':'https://www.youtube.com/watch?v=rW1jPlYgp_0',
                    'Video_3':'https://www.youtube.com/watch?v=ckCkaiN9Wlg',
                },
                {
                    'title':'Network Addressing',
                    'image':'https://i.pinimg.com/736x/e8/4f/cc/e84fcc53a804c981fff96dfbd9f7a8b7.jpg',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/network_addressing.htm',
                    'text':'Layer 3 network addressing is one of the major tasks of Network Layer. Network Addresses are always logical i.e. these are software based addresses which can be changed by appropriate configurations.',
                    'Video_1':'https://www.youtube.com/watch?v=yDTC6sbYFFE',
                    'Video_2':'https://www.youtube.com/watch?v=yuPST5jEEJg',
                    'Video_3':'https://www.youtube.com/watch?v=Kx6i9gwNS3w',
                },
                {
                    'title':'Network Layer Routing',
                    'image':'https://i.pinimg.com/736x/e8/4f/cc/e84fcc53a804c981fff96dfbd9f7a8b7.jpg',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/network_layer_routing.htm',
                    'text':'When a device has multiple paths to reach a destination, it always selects one path by preferring it over others. This selection process is termed as Routing. Routing is done by special network devices called routers or it can be done by means of software processes.The software based routers have limited functionality and limited scope.',
                    'Video_1':'https://www.youtube.com/watch?v=rA0p0ouD3aE',
                    'Video_2':'https://www.youtube.com/watch?v=xwaqSZHK8eM',
                    'Video_3':'https://www.youtube.com/watch?v=3djoAM-3MM4',
                },
                {
                    'title':'Internetworking',
                    'image':'https://i.pinimg.com/736x/e8/4f/cc/e84fcc53a804c981fff96dfbd9f7a8b7.jpg',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/internetworking.htm',
                    'text':'In real world scenario, networks under same administration are generally scattered geographically. There may exist requirement of connecting two different networks of same kind as well as of different kinds. Routing between two networks is called internetworking.',
                    'Video_1':'https://www.youtube.com/watch?v=dFw_k7entc4',
                    'Video_2':'https://www.youtube.com/watch?v=qpxo8SKU5Bc',
                    'Video_3':'https://www.youtube.com/watch?v=ebyQ4fNs2y0',
                },
                {
                    'title':'Network Layer Protocols',
                    'image':'https://i.pinimg.com/736x/e8/4f/cc/e84fcc53a804c981fff96dfbd9f7a8b7.jpg',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/network_layer_protocols.htm',
                    'text':'Every computer in a network has an IP address by which it can be uniquely identified and addressed. An IP address is Layer-3 (Network Layer) logical address. This address may change every time a computer restarts. A computer can have one IP at one instance of time and another IP at some different time.',
                    'Video_1':'https://www.youtube.com/watch?v=JvrgljAHO5w',
                    'Video_2':'https://www.youtube.com/watch?v=STRTJLdVNU4',
                    'Video_3':'https://www.youtube.com/watch?v=L5aEQTF_NkM',
                }
        ]
    }

posts_process={
    'articles':[
                {
                    'title':'Process Vs Program',
                    'image':'https://safebytes.com/wp-content/uploads/2016/12/operating_system1600.png',
                    'content':'https://www.geeksforgeeks.org/introduction-of-process-management/',
                    'text':'A process is basically a program in execution. The execution of a process must progress in a sequential fashion.A process is defined as an entity which represents the basic unit of work to be implemented in the system.',
                    'Video_1':'https://www.youtube.com/watch?v=c0HbxwfxeMM',
                    'Video_2':'https://www.youtube.com/watch?v=grriYn6v76g',
                    'Video_3':'https://www.youtube.com/watch?v=ucVm_arB-fw',
                },
                {
                    'title':'Process Control Block (PCB)',
                    'image':'https://safebytes.com/wp-content/uploads/2016/12/operating_system1600.png',
                    'content':'https://www.tutorialspoint.com/data_communication_computer_network/network_addressing.htm',
                    'text':'A Process Control Block is a data structure maintained by the Operating System for every process. The PCB is identified by an integer process ID (PID).',
                    'Video_1':'https://www.youtube.com/watch?v=4s2MKuVYKV8',
                    'Video_2':'https://www.youtube.com/watch?v=zInSLmBc81g',
                    'Video_3':'https://www.youtube.com/watch?v=ssRZqodkoac',
                }
        ]
    }

posts_schedule={
    'articles':[
                {
                    'title':'Process Scheduling Queues',
                    'image':'https://safebytes.com/wp-content/uploads/2016/12/operating_system1600.png',
                    'content':'https://www.guru99.com/process-scheduling.html',
                    'text':'The OS maintains all PCBs in Process Scheduling Queues. The OS maintains a separate queue for each of the process states and PCBs of all processes in the same execution state are placed in the same queue. When the state of a process is changed, its PCB is unlinked from its current queue and moved to its new state queue.',
                    'Video_1':'https://www.youtube.com/watch?v=2h3eWaPx8SA',
                    'Video_2':'https://www.youtube.com/watch?v=J4NYr0xjTic',
                    'Video_3':'https://www.youtube.com/watch?v=2dJdHMpCLIg',
                },
                {
                    'title':'Context Switch',
                    'image':'https://safebytes.com/wp-content/uploads/2016/12/operating_system1600.png',
                    'content':'https://www.tutorialspoint.com/what-is-context-switching-in-operating-system',
                    'text':'A context switch is the mechanism to store and restore the state or context of a CPU in Process Control block so that a process execution can be resumed from the same point at a later time. Using this technique, a context switcher enables multiple processes to share a single CPU. Context switching is an essential part of a multitasking operating system features.',
                    'Video_1':'https://www.youtube.com/watch?v=vTgccrbYHYs',
                    'Video_2':'https://www.youtube.com/watch?v=DKmBRl8j3Ak',
                    'Video_3':'https://www.youtube.com/watch?v=bId-MwXiDaI',
                }
        ]
    }

posts_algorithms={
    'articles':[
                {
                    'title':'First Come First Serve (FCFS)',
                    'image':'https://www.kindpng.com/picc/m/41-419243_logo-appointment-scheduling-icon-hd-png-download.png',
                    'content':'https://www.studytonight.com/operating-system/first-come-first-serve',
                    'text':'In the "First come first serve" scheduling algorithm, as the name suggests, the process which arrives first, gets executed first, or we can say that the process which requests the CPU first, gets the CPU allocated first.',
                    'Video_1':'https://www.youtube.com/watch?v=MZdVAVMgNpA',
                    'Video_2':'https://www.youtube.com/watch?v=HIB3hZ-5fHw',
                    'Video_3':'https://www.youtube.com/watch?v=7DoP1L9nAAs',
                },
                {
                    'title':'Shortest Job Next (SJN)',
                    'image':'https://www.kindpng.com/picc/m/41-419243_logo-appointment-scheduling-icon-hd-png-download.png',
                    'content':'https://www.guru99.com/shortest-job-first-sjf-scheduling.html',
                    'text':'Shortest Job First (SJF) is an algorithm in which the process having the smallest execution time is chosen for the next execution. This scheduling method can be preemptive or non-preemptive. It significantly reduces the average waiting time for other processes awaiting execution. The full form of SJF is Shortest Job First. ',
                    'Video_1':'https://www.youtube.com/watch?v=VCIVXPoiLpU',
                    'Video_2':'https://www.youtube.com/watch?v=t0g9b3SJECg',
                    'Video_3':'https://www.youtube.com/watch?v=xh8hRjtbu3k',
                },
                {
                    'title':'Priority Based Scheduling',
                    'image':'https://www.kindpng.com/picc/m/41-419243_logo-appointment-scheduling-icon-hd-png-download.png',
                    'content':'https://www.guru99.com/priority-scheduling-program.html',
                    'text':'Priority Scheduling is a method of scheduling processes that is based on priority. In this algorithm, the scheduler selects the tasks to work as per the priority.',
                    'Video_1':'https://www.youtube.com/watch?v=rsDGfFxSgiY',
                    'Video_2':'https://www.youtube.com/watch?v=i4PQucowf1c',
                    'Video_3':'https://www.youtube.com/watch?v=hDn4hM148V8',
                },
                {
                    'title':'Shortest Remaining Time',
                    'image':'https://www.kindpng.com/picc/m/41-419243_logo-appointment-scheduling-icon-hd-png-download.png',
                    'content':'https://www.javatpoint.com/os-srtf-scheduling-algorithm',
                    'text':'This Algorithm is the preemptive version of SJF scheduling. In SRTF, the execution of the process can be stopped after certain amount of time. At the arrival of every process, the short term scheduler schedules the process with the least remaining burst time among the list of available processes and the running process.',
                    'Video_1':'https://www.youtube.com/watch?v=YxbldXw1FLM',
                    'Video_2':'https://www.youtube.com/watch?v=wx0uNkMI7Lk',
                    'Video_3':'https://www.youtube.com/watch?v=klTGGxTyk78',
                },
                {
                    'title':'Round Robin Scheduling',
                    'image':'https://www.kindpng.com/picc/m/41-419243_logo-appointment-scheduling-icon-hd-png-download.png',
                    'content':'https://www.guru99.com/round-robin-scheduling-example.html',
                    'text':'The name of this algorithm comes from the round-robin principle, where each person gets an equal share of something in turns. It is the oldest, simplest scheduling algorithm, which is mostly used for multitasking.',
                    'Video_1':'https://www.youtube.com/watch?v=TxjIlNYRZ5M',
                    'Video_2':'https://www.youtube.com/watch?v=YzBBJYfwdi8',
                    'Video_3':'https://www.youtube.com/watch?v=vuBt54W3hXk',
                },
                {
                    'title':'Multiple-Level Queues Scheduling',
                    'image':'https://www.kindpng.com/picc/m/41-419243_logo-appointment-scheduling-icon-hd-png-download.png',
                    'content':'https://www.geeksforgeeks.org/multilevel-queue-mlq-cpu-scheduling/',
                    'text':'Multiple-level queues are not an independent scheduling algorithm. They make use of other existing algorithms to group and schedule jobs with common characteristics.',
                    'Video_1':'https://www.youtube.com/watch?v=hBPYP0ZEvS8',
                    'Video_2':'https://www.youtube.com/watch?v=fvkSXMZaBNY',
                    'Video_3':'https://www.youtube.com/watch?v=1w9FybdNi_Y',
                }
        ]
    }

posts_virtual={
    'articles':[
                {
                    'title':'Introduction',
                    'image':'https://as1.ftcdn.net/jpg/01/69/92/92/500_F_169929275_cNDa0pGk5PZqAZST6FysFu8YQ1iEauO2.jpg',
                    'content':'https://www.geeksforgeeks.org/virtual-memory-in-operating-system/',
                    'text':'Virtual Memory is a storage allocation scheme in which secondary memory can be addressed as though it were part of main memory. The addresses a program may use to reference memory are distinguished from the addresses the memory system uses to identify physical storage sites, and program generated addresses are translated automatically to the corresponding machine addresses.',
                    'Video_1':'https://www.youtube.com/watch?v=o2_iCzS9-ZQ',
                    'Video_2':'https://www.youtube.com/watch?v=2quKyPnUShQ',
                    'Video_3':'https://www.youtube.com/watch?v=kCmu5k6jfXM',
                },
                {
                    'title':'Demand Paging',
                    'image':'https://as1.ftcdn.net/jpg/01/69/92/92/500_F_169929275_cNDa0pGk5PZqAZST6FysFu8YQ1iEauO2.jpg',
                    'content':'https://www.javatpoint.com/os-demand-paging',
                    'text':'According to the concept of Virtual Memory, in order to execute some process, only a part of the process needs to be present in the main memory which means that only a few pages will only be present in the main memory at any time. ',
                    'Video_1':'https://www.youtube.com/watch?v=501Xm6swx2Q',
                    'Video_2':'https://www.youtube.com/watch?v=JZ6ocz3Dess',
                    'Video_3':'https://www.youtube.com/watch?v=4KFZMaCenX4',
                },
                {
                    'title':'First In First Out (FIFO) algorithm',
                    'image':'https://as1.ftcdn.net/jpg/01/69/92/92/500_F_169929275_cNDa0pGk5PZqAZST6FysFu8YQ1iEauO2.jpg',
                    'content':'https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/',
                    'text':'In operating systems, whenever a new page is referred and not present in memory, page fault occurs and Operating System replaces one of the existing pages with newly needed page. Different page replacement algorithms suggest different ways to decide which page to replace. The target for all algorithms is to reduce number of page faults.',
                    'Video_1':'https://www.youtube.com/watch?v=8rcUs5RutX0',
                    'Video_2':'https://www.youtube.com/watch?v=ET43MRKRuYM',
                    'Video_3':'https://www.youtube.com/watch?v=EeXEuUe1b1A',
                },
                {
                    'title':'Optimal Page Replacement Algorithm',
                    'image':'https://as1.ftcdn.net/jpg/01/69/92/92/500_F_169929275_cNDa0pGk5PZqAZST6FysFu8YQ1iEauO2.jpg',
                    'content':'https://www.javatpoint.com/os-srtf-scheduling-algorithm',
                    'text':'This Algorithm is the preemptive version of SJF scheduling. In SRTF, the execution of the process can be stopped after certain amount of time. At the arrival of every process, the short term scheduler schedules the process with the least remaining burst time among the list of available processes and the running process.',
                    'Video_1':'https://www.youtube.com/watch?v=q2BpMvPhhrY',
                    'Video_2':'https://www.youtube.com/watch?v=6T2F6KMDvt4',
                    'Video_3':'https://www.youtube.com/watch?v=L8BEoRRUVRE',
                },
                {
                    'title':'Least Recently Used (LRU) algorithm',
                    'image':'https://as1.ftcdn.net/jpg/01/69/92/92/500_F_169929275_cNDa0pGk5PZqAZST6FysFu8YQ1iEauO2.jpg',
                    'content':'https://www.geeksforgeeks.org/program-for-least-recently-used-lru-page-replacement-algorithm/',
                    'text':'Page which has not been used for the longest time in main memory is the one which will be selected for replacement.',
                    'Video_1':'https://www.youtube.com/watch?v=dYIoWkCvd6A',
                    'Video_2':'https://www.youtube.com/watch?v=4wVp97-uqr0',
                    'Video_3':'https://www.youtube.com/watch?v=LCPFjNxQIVU',
                },
                {
                    'title':'Least frequently Used(LFU) algorithm',
                    'image':'https://as1.ftcdn.net/jpg/01/69/92/92/500_F_169929275_cNDa0pGk5PZqAZST6FysFu8YQ1iEauO2.jpg',
                    'content':'https://www.geeksforgeeks.org/least-frequently-used-lfu-cache-implementation/',
                    'text':'Least Frequently Used (LFU) is a caching algorithm in which the least frequently used cache block is removed whenever the cache is overflowed. In LFU we check the old page as well as the frequency of that page and if the frequency of the page is larger than the old page we cannot remove it and if all the old pages are having same frequency then take last i.e FIFO method for that and remove that page.',
                    'Video_1':'https://www.youtube.com/watch?v=9V4mzK-RaP8',
                    'Video_2':'https://www.youtube.com/watch?v=PQgEpWREIcY',
                    'Video_3':'https://www.youtube.com/watch?v=W50KI8777eM',
                },
        ]
    }

posts_other={
    'articles':[
                {
                    'title':'Multi-Threading',
                    'image':'https://thumbs.dreamstime.com/b/multithreading-icon-vector-illustration-multithreading-icon-vector-illustration-feather-white-background-119471041.jpg',
                    'content':'https://www.tutorialspoint.com/operating_system/os_multi_threading.htm',
                    'text':'A thread is a flow of execution through the process code, with its own program counter that keeps track of which instruction to execute next, system registers which hold its current working variables, and a stack which contains the execution history.',
                    'Video_1':'https://www.youtube.com/watch?v=TG9jXum0jSY',
                    'Video_2':'https://www.youtube.com/watch?v=LOfGJcVnvAk',
                    'Video_3':'https://www.youtube.com/watch?v=HW2Wcx-ktsc',
                },
                {
                    'title':'Memory Management',
                    'image':'https://juliagpu.gitlab.io/CUDA.jl/assets/logo.png',
                    'content':'https://www.tutorialspoint.com/operating_system/os_memory_management.htm',
                    'text':'Memory management is the functionality of an operating system which handles or manages primary memory and moves processes back and forth between main memory and disk during execution. Memory management keeps track of each and every memory location, regardless of either it is allocated to some process or it is free.',
                    'Video_1':'https://www.youtube.com/watch?v=eESIFJz7mJw',
                    'Video_2':'https://www.youtube.com/watch?v=FrTttJLN7Kw',
                    'Video_3':'https://www.youtube.com/watch?v=SQZbTmAoEYM',
                },
                {
                    'title':'I/O Hardware',
                    'image':'http://2.bp.blogspot.com/-yxIPZvUIwW8/U0d2JeSVQII/AAAAAAAAApI/9COLdc6Xp8g/s1600/RAID1-jpg.jpg',
                    'content':'https://www.tutorialspoint.com/operating_system/os_io_hardware.htm',
                    'text':'One of the important jobs of an Operating System is to manage various I/O devices including mouse, keyboards, touch pad, disk drives, display adapters, USB devices, Bit-mapped screen, LED, Analog-to-digital converter, On/off switch, network connections, audio I/O, printers etc.',
                    'Video_1':'https://www.youtube.com/watch?v=F18RiREDkwE',
                    'Video_2':'https://www.youtube.com/watch?v=ReRj0Ww0TU4',
                    'Video_3':'https://www.youtube.com/watch?v=DYGrqNBWymw',
                },
                {
                    'title':'I/O Softwares',
                    'image':'https://iodigital.io/wp-content/uploads/2016/06/iocoin.png',
                    'content':'https://www.tutorialspoint.com/operating_system/os_io_software.htm',
                    'text':'A key concept in the design of I/O software is that it should be device independent where it should be possible to write programs that can access any I/O device without having to specify the device in advance.',
                    'Video_1':'https://www.youtube.com/watch?v=EJfsCCXNN9o',
                    'Video_2':'https://www.youtube.com/watch?v=gwqmsqQBW6Y',
                },
                {
                    'title':'File System',
                    'image':'https://icon-library.com/images/file-system-icon/file-system-icon-25.jpg',
                    'content':'https://www.tutorialspoint.com/operating_system/os_file_system.htm',
                    'text':'A file is a named collection of related information that is recorded on secondary storage such as magnetic disks, magnetic tapes and optical disks. In general, a file is a sequence of bits, bytes, lines or records whose meaning is defined by the files creator and user.',
                    'Video_1':'https://www.youtube.com/watch?v=0LtuQhNFFe0',
                    'Video_2':'https://www.youtube.com/watch?v=_h30HBYxtws',
                    'Video_3':'https://www.youtube.com/watch?v=mzUyMy7Ihk0',
                }
        ]
    }

posts_intro={
    'articles':[
                {
                    'title':'Architecture',
                    'image':'https://www.w3schools.in/wp-content/uploads/dbms-logo.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_architecture.htm',
                    'text':'The design of a DBMS depends on its architecture. It can be centralized or decentralized or hierarchical. The architecture of a DBMS can be seen as either single tier or multi-tier. An n-tier architecture divides the whole system into related but independent n modules, which can be independently modified, altered, changed, or replaced.',
                    'Video_1':'https://www.youtube.com/watch?v=VyvTabQHevw',
                    'Video_2':'https://www.youtube.com/watch?v=L8Vqu7yhmGg',
                    'Video_3':'https://www.youtube.com/watch?v=AAKUqHBuzk4',
                },
                {
                    'title':'Data Models',
                    'image':'https://www.w3schools.in/wp-content/uploads/dbms-logo.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_data_models.htm',
                    'text':'Data models define how the logical structure of a database is modeled. Data Models are fundamental entities to introduce abstraction in a DBMS. Data models define how data is connected to each other and how they are processed and stored inside the system.',
                    'Video_1':'https://www.youtube.com/watch?v=ow4rUuqsDbI',
                    'Video_2':'https://www.youtube.com/watch?v=OQanW4NVksY',
                    'Video_3':'https://www.youtube.com/watch?v=o1HLZRtFwxk',
                },
                {
                    'title':'Data Schemas',
                    'image':'https://www.w3schools.in/wp-content/uploads/dbms-logo.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_data_schemas.htm',
                    'text':'A database schema is the skeleton structure that represents the logical view of the entire database. It defines how the data is organized and how the relations among them are associated. It formulates all the constraints that are to be applied on the data.',
                    'Video_1':'https://www.youtube.com/watch?v=pDX4NR4eY3A',
                    'Video_2':'https://www.youtube.com/watch?v=rq6e9AeWRtE',
                    'Video_3':'https://www.youtube.com/watch?v=5fs1ldO6B5c',
                },
                {
                    'title':'Data Independence',
                    'image':'https://www.w3schools.in/wp-content/uploads/dbms-logo.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_data_independence.htm',
                    'text':'If a database system is not multi-layered, then it becomes difficult to make any changes in the database system. Database systems are designed in multi-layers as we learnt earlier.',
                    'Video_1':'https://www.youtube.com/watch?v=upUSGUSK5k0',
                    'Video_2':'https://www.youtube.com/watch?v=JT2uTWuZaYw',
                }
        ]
    } 

posts_er_models={
    'articles':[
                {
                    'title':'Basic Concepts',
                    'image':'https://cdn2.iconfinder.com/data/icons/computer-science-butterscotch-vol-1/512/ERD-512.png',
                    'content':'https://www.tutorialspoint.com/dbms/er_model_basic_concepts.htm',
                    'text':'The ER model defines the conceptual view of a database. It works around real-world entities and the associations among them. At view level, the ER model is considered a good option for designing databases.',
                    'Video_1':'https://www.youtube.com/watch?v=gbVev8RuZLg',
                    'Video_2':'https://www.youtube.com/watch?v=Wv1c9K4788A',
                    'Video_3':'https://www.youtube.com/watch?v=QpdhBUYk7Kk',
                },
                {
                    'title':'Diagram Representation',
                    'image':'https://cdn2.iconfinder.com/data/icons/computer-science-butterscotch-vol-1/512/ERD-512.png',
                    'content':'https://www.tutorialspoint.com/dbms/er_diagram_representation.htm',
                    'text':'Let us now learn how the ER Model is represented by means of an ER diagram. Any object, for example, entities, attributes of an entity, relationship sets, and attributes of relationship sets, can be represented with the help of an ER diagram.',
                    'Video_1':'https://www.youtube.com/watch?v=obb7SlUmKQE',
                    'Video_2':'https://www.youtube.com/watch?v=3GpwG6Q7zpc',
                    'Video_3':'https://www.youtube.com/watch?v=nmDpnm8RtdI',
                },
                {
                    'title':'Generalization Aggregation',
                    'image':'https://cdn2.iconfinder.com/data/icons/computer-science-butterscotch-vol-1/512/ERD-512.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_generalization_aggregation.htm',
                    'text':'The ER Model has the power of expressing database entities in a conceptual hierarchical manner. As the hierarchy goes up, it generalizes the view of entities, and as we go deep in the hierarchy, it gives us the detail of every entity included.',
                    'Video_1':'https://www.youtube.com/watch?v=H2AGn0QHcSI',
                    'Video_2':'https://www.youtube.com/watch?v=4_vsGgy9cGs',
                    'Video_3':'https://www.youtube.com/watch?v=3HIX92Ce1Uo',
                }
        ]
    }  

posts_models={
    'articles':[
                {
                    'title':"Codd's 12 Rules",
                    'image':'https://www.pngitem.com/pimgs/m/499-4996899_database-relation-icon-png-transparent-png.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_codds_rules.htm',
                    'text':'Dr Edgar F. Codd, after his extensive research on the Relational Model of database systems, came up with twelve rules of his own, which according to him, a database must obey in order to be regarded as a true relational database.',
                    'Video_1':'https://www.youtube.com/watch?v=5YeZruwP6go',
                    'Video_2':'https://www.youtube.com/watch?v=RtYyY5RreBs',
                    'Video_3':'https://www.youtube.com/watch?v=Oj89F1KDYJ8',
                },
                {
                    'title':'Relation Data Model',
                    'image':'https://www.pngitem.com/pimgs/m/499-4996899_database-relation-icon-png-transparent-png.png',
                    'content':'https://www.tutorialspoint.com/dbms/relational_data_model.htm',
                    'text':'Relational data model is the primary data model, which is used widely around the world for data storage and processing. This model is simple and it has all the properties and capabilities required to process data with storage efficiency.',
                    'Video_1':'https://www.youtube.com/watch?v=4YilEjkNPrQ',
                    'Video_2':'https://www.youtube.com/watch?v=wB0JBqWKxBw',
                    'Video_3':'https://www.youtube.com/watch?v=3EJlovevfcA',
                },
                {
                    'title':'Relational Algebra',
                    'image':'https://www.pngitem.com/pimgs/m/499-4996899_database-relation-icon-png-transparent-png.png',
                    'content':'https://www.tutorialspoint.com/dbms/relational_algebra.htm',
                    'text':'Relational database systems are expected to be equipped with a query language that can assist its users to query the database instances. There are two kinds of query languages − relational algebra and relational calculus.',
                    'Video_1':'https://www.youtube.com/watch?v=wbiZiEpHAZY',
                    'Video_2':'https://www.youtube.com/watch?v=brZs_8Jpuc0',
                    'Video_3':'https://www.youtube.com/watch?v=5oN4nXa1d_k',
                },
                {
                    'title':'ER Model to Relational Model',
                    'image':'https://www.pngitem.com/pimgs/m/499-4996899_database-relation-icon-png-transparent-png.png',
                    'content':'https://www.tutorialspoint.com/dbms/er_model_to_relational_model.htm',
                    'text':'ER Model, when conceptualized into diagrams, gives a good overview of entity-relationship, which is easier to understand. ER diagrams can be mapped to relational schema, that is, it is possible to create relational schema using ER diagram. We cannot import all the ER constraints into relational model, but an approximate schema can be generated.',
                    'Video_1':'https://www.youtube.com/watch?v=CZTkgMoqVss',
                    'Video_2':'https://www.youtube.com/watch?v=OwdFzygGZqk',
                    'Video_3':'https://www.youtube.com/watch?v=3DcAo6ZdOlA',
                },
                {
                    'title':'SQL Overview',
                    'image':'https://www.pngitem.com/pimgs/m/499-4996899_database-relation-icon-png-transparent-png.png',
                    'content':'https://www.tutorialspoint.com/dbms/sql_overview.htm',
                    'text':'SQL is a programming language for Relational Databases. It is designed over relational algebra and tuple relational calculus. SQL comes as a package with all major distributions of RDBMS.',
                    'Video_1':'https://www.youtube.com/watch?v=323H_mOOWQ4',
                    'Video_2':'https://www.youtube.com/watch?v=27axs9dO7AE',
                    'Video_3':'https://www.youtube.com/watch?v=zbMHLJ0dY4w',
                }
        ]
    }

posts_rdbms={
    'articles':[
                {
                    'title':"Normalization",
                    'image':'https://img.favpng.com/18/9/15/relational-database-management-system-sql-png-favpng-YtEuZw3ZX3FatXhLkXAVsvi8t.jpg',
                    'content':'https://www.tutorialspoint.com/dbms/database_normalization.htm',
                    'text':'Functional dependency (FD) is a set of constraints between two attributes in a relation. Functional dependency says that if two tuples have same values for attributes A1, A2,..., An, then those two tuples must have to have same values for attributes B1, B2, ..., Bn.',
                    'Video_1':'https://www.youtube.com/watch?v=5GDTIUVlHB8',
                    'Video_2':'https://www.youtube.com/watch?v=ABwD8IYByfk',
                    'Video_3':'https://www.youtube.com/watch?v=xoTyrdT9SZI',
                },
                {
                    'title':'Joins',
                    'image':'https://img.favpng.com/18/9/15/relational-database-management-system-sql-png-favpng-YtEuZw3ZX3FatXhLkXAVsvi8t.jpg',
                    'content':'https://www.tutorialspoint.com/dbms/database_joins.htm',
                    'text':'We understand the benefits of taking a Cartesian product of two relations, which gives us all the possible tuples that are paired together. But it might not be feasible for us in certain cases to take a Cartesian product where we encounter huge relations with thousands of tuples having a considerable large number of attributes.',
                    'Video_1':'https://www.youtube.com/watch?v=zYH-e6tUYbw',
                    'Video_2':'https://www.youtube.com/watch?v=bLL5NbBEg2I',
                    'Video_3':'https://www.youtube.com/watch?v=hIh5-Y1QwFw',
                }
        ]
    }


#yahaa se karna hai



posts_file={
    'articles':[
                {
                    'title':"Storage System",
                    'image':'https://cdn3.iconfinder.com/data/icons/ultimate-social/150/15_google_drive-512.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_storage_system.htm',
                    'text':'Databases are stored in file formats, which contain records. At physical level, the actual data is stored in electromagnetic format on some device. These storage devices can be broadly categorized into three types −',
                    'Video_1':'https://www.youtube.com/watch?v=WeiyF5NjUzc',
                    'Video_2':'https://www.youtube.com/watch?v=YcRd3WMbXnE',
                    'Video_3':'https://www.youtube.com/watch?v=bjIEw15FKs8',
                },
                {
                    'title':'File Structure',
                    'image':'https://cdn3.iconfinder.com/data/icons/ultimate-social/150/15_google_drive-512.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_file_structure.htm',
                    'text':'Relative data and information is stored collectively in file formats. A file is a sequence of records stored in binary format. A disk drive is formatted into several blocks that can store records. File records are mapped onto those disk blocks.',
                    'Video_1':'https://www.youtube.com/watch?v=ZtVw2iuFI2w',
                    'Video_2':'https://www.youtube.com/watch?v=eX5mdzKtX30',
                    'Video_3':'https://www.youtube.com/watch?v=JM7yx8X6bj4',
                }
        ]
    }


posts_index={
    'articles':[
                {
                    'title':"Indexing",
                    'image':'https://cdn4.iconfinder.com/data/icons/cryptocurrency-bitcoin-and-blockchain/32/cryptocurrency_bitcoin_hashing_hash_function-512.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_indexing.htm',
                    'text':'Indexing is a data structure technique to efficiently retrieve records from the database files based on some attributes on which the indexing has been done. Indexing in database systems is similar to what we see in books.',
                    'Video_1':'https://www.youtube.com/watch?v=E--yzX05_k8',
                    'Video_2':'https://www.youtube.com/watch?v=LOfGJcVnvAk',
                    'Video_3':'https://www.youtube.com/watch?v=HW2Wcx-ktsc',
                },
                {
                    'title':'Hashing',
                    'image':'https://cdn4.iconfinder.com/data/icons/cryptocurrency-bitcoin-and-blockchain/32/cryptocurrency_bitcoin_hashing_hash_function-512.png',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_hashing.htm',
                    'text':'For a huge database structure, it can be almost next to impossible to search all the index values through all its level and then reach the destination data block to retrieve the desired data. Hashing is an effective technique to calculate the direct location of a data record on the disk without using index structure.',
                    'Video_1':'https://www.youtube.com/watch?v=eESIFJz7mJw',
                    'Video_2':'https://www.youtube.com/watch?v=vjrHiaIfOl8',
                    'Video_3':'https://www.youtube.com/watch?v=lyTPtoBfs9I',
                }
        ]
    }

posts_backup={
    'articles':[
                {
                    'title':"Data Backup",
                    'image':'https://banner2.cleanpng.com/20181125/uzh/kisspng-computer-icons-backup-and-restore-clip-art-databas-5bfae2143ce388.5626160015431685322494.jpg',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_data_backup.htm',
                    'text':'A volatile storage like RAM stores all the active logs, disk buffers, and related data. In addition, it stores all the transactions that are being currently executed. What happens if such a volatile storage crashes abruptly? It would obviously take away all the logs and active copies of the database. It makes recovery almost impossible, as everything that is required to recover the data is lost.',
                    'Video_1':'https://www.youtube.com/watch?v=aAtBR0sfVfg',
                    'Video_2':'https://www.youtube.com/watch?v=0YhOYqPeq0g',
                    'Video_3':'https://www.youtube.com/watch?v=o-83E6levzM',
                },
                {
                    'title':'Data Recovery',
                    'image':'https://banner2.cleanpng.com/20181125/uzh/kisspng-computer-icons-backup-and-restore-clip-art-databas-5bfae2143ce388.5626160015431685322494.jpg',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_data_recovery.htm',
                    'text':'DBMS is a highly complex system with hundreds of transactions being executed every second. The durability and robustness of a DBMS depends on its complex architecture and its underlying hardware and system software. If it fails or crashes amid transactions, it is expected that the system would follow some sort of algorithm or techniques to recover lost data.',
                    'Video_1':'https://www.youtube.com/watch?v=v5qKiXa36o4',
                    'Video_2':'https://www.youtube.com/watch?v=ls3gGWg8W4E',
                    'Video_3':'https://www.youtube.com/watch?v=FcxLR4iWZm4',
                }
        ]
    }

posts_concurrent={
    'articles':[
                {
                    'title':'Transaction',
                    'image':'https://cdn.imgbin.com/25/21/0/imgbin-computer-icons-database-data-access-microsoft-access-others-uF5zNDvAqfAAucq69ZkZRzyDn.jpg',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_transaction.htm',
                    'text':'A transaction can be defined as a group of tasks. A single task is the minimum processing unit which cannot be divided further.',
                    'Video_1':'https://www.youtube.com/watch?v=t5hsV9lC1rU',
                    'Video_2':'https://www.youtube.com/watch?v=-GS0OxFJsYQ',
                    'Video_3':'https://www.youtube.com/watch?v=ObwYFVLB_VI',
                },
                {
                    'title':'Concurrency Control',
                    'image':'https://cdn.imgbin.com/25/21/0/imgbin-computer-icons-database-data-access-microsoft-access-others-uF5zNDvAqfAAucq69ZkZRzyDn.jpg',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_concurrency_control.htm',
                    'text':'In a multiprogramming environment where multiple transactions can be executed simultaneously, it is highly important to control the concurrency of transactions. We have concurrency control protocols to ensure atomicity, isolation, and serializability of concurrent transactions.',
                    'Video_1':'https://www.youtube.com/watch?v=94C0V7f2zm4',
                    'Video_2':'https://www.youtube.com/watch?v=UsqtDD1VriY',
                    'Video_3':'https://www.youtube.com/watch?v=Thm0xW9oTow',
                },
                {
                    'title':'Deadlock',
                    'image':'https://cdn.imgbin.com/25/21/0/imgbin-computer-icons-database-data-access-microsoft-access-others-uF5zNDvAqfAAucq69ZkZRzyDn.jpg',
                    'content':'https://www.tutorialspoint.com/dbms/dbms_deadlock.htm',
                    'text':'In a multi-process system, deadlock is an unwanted situation that arises in a shared resource environment, where a process indefinitely waits for a resource that is held by another process.Deadlocks are not healthy for a system. In case a system is stuck in a deadlock, the transactions involved in the deadlock are either rolled back or restarted.',
                    'Video_1':'https://www.youtube.com/watch?v=rWFH6PLOIEI',
                    'Video_2':'https://www.youtube.com/watch?v=pPM9Ajqmy_4',
                    'Video_3':'https://www.youtube.com/watch?v=4KPEzu92ZWI',
                }
        ]
    } 

@app.route('/ds_algo/Algorithms')
def algo():
    return jsonify(posts_algo)

@app.route('/ds_algo/Data Structures')
def ds():
    return jsonify(posts_ds)

@app.route('/computer_networks/Data Link Layer')
def data():
    return jsonify(posts_data)

@app.route('/computer_networks/Application Layer')
def application():
    return jsonify(posts_application)

@app.route('/computer_networks/Transport Layer')
def transport():
    return jsonify(posts_transport)

@app.route('/computer_networks/Network Layer')
def network():
    return jsonify(posts_networks)

@app.route('/operating_system/Process')
def process():
    return jsonify(posts_process)

@app.route('/operating_system/Process Scheduling')
def schedule():
    return jsonify(posts_schedule)

@app.route('/operating_system/Scheduling Algorithms')
def schedule_algo():
    return jsonify(posts_algorithms)

@app.route('/operating_system/Virtual Memory')
def memory():
    return jsonify(posts_virtual)

@app.route('/operating_system/Other topics')
def other():
    return jsonify(posts_other)

@app.route('/dbms/Introduction')
def intro():
    return jsonify(posts_intro)

@app.route('/dbms/ER Model')
def er_model():
    return jsonify(posts_er_models)

@app.route('/dbms/Relation Model')
def rmodel():
    return jsonify(posts_models)

@app.route('/dbms/Relational Database')
def rdbms():
    return jsonify(posts_rdbms)

@app.route('/dbms/File Structure')
def structure():
    return jsonify(posts_file)

@app.route('/dbms/Indexing & Hashing')
def index():
    return jsonify(posts_index)

@app.route('/dbms/Concurrency')
def concurrent():
    return jsonify(posts_concurrent)

@app.route('/dbms/Backup Recovery')
def recovery():
    return jsonify(posts_backup)


if(__name__)=="__main__":
    app.run()
