
#include <algorithm>
#include <queue>
#include <cassert>


/// This class represents one node of a Binary search tree.
class Node
{
private:
	int _value;
	Node* _left = nullptr;
	Node* _right = nullptr;
	Node* _parent = nullptr;

public:
	/// Constructor
	/// Creates a leaf node with specified value.
	explicit Node( int value_ = 0 )
		: _value( value_ )
		{}

	/// Constructor
	/// Creates a node and attaches already constructed 2 subtrees
	///    to it.
	Node( int value_, Node* left_, Node* right_ )
		: _value( value_ ), 
		  _left( left_ ), 
		  _right( right_ ) {
		_left->_parent = this;
		_right->_parent = this;
	}

	/// Destructor
	~Node() {
		delete _right;
		delete _left;
	}

	/// Inserts value 'x' as a new node, in the subtree starting 
	/// from 'this' node.
	void insert( int x ) {
		Node* p = this;
		while ( true ) {
			if ( x < p->_value ) {  // Must go left
				if ( p->_left == nullptr ) {
					p->_left = new Node( x );
					p->_left->_parent = p;
					break;
				}
				else {
					p = p->_left;
				}
			}
			else {  // Must go right
				if ( p->_right == nullptr ) {
					p->_right = new Node( x );
					p->_right->_parent = p;
					break;
				}
				else {
					p = p->_right;
				}
			}
		}
	}

	/// Flips the subtree, starting from 'this' node.
	void flip_recursive() {
		if ( this == nullptr )
			return;
		// Flip this node
		std::swap( _left, _right );
		// Flip subtrees
		_left->flip_recursive();
		_right->flip_recursive();
	}

	/// Flips the subtree, starting from 'this' node.
	void flip_iterative() {
		std::queue< Node* > q;
		q.push( this );
		while ( ! q.empty() ) {
			// Take first node from the queue
			Node* n = q.front();
			q.pop();
			// Flip it
			std::swap( n->_left, n->_right );
			// Add its child nodes to the queue, for later processing
			if ( n->_left )
				q.push( n->_left );
			if ( n->_right )
				q.push( n->_right );
		}
	}

	friend void remove_leaf( Node* node );
	friend void remove_1_child_node( Node* node );
	friend void remove_2_child_node( Node* node );
	friend void remove_node( Node* node );
};


/// Removes specified 'node' from binary search tree, expecting that 
/// it is a leaf node.
void remove_leaf( Node* node )
{
	// Check that provided argument is a leaf
	assert( node->_left == nullptr && node->_right == nullptr );
	// Unlink from parent
	Node* p = node->_parent;
	if ( p != nullptr ) {
		if ( node == p->_left )
			p->_left = nullptr;
		else
			p->_right = nullptr;
	}
	// Perform deletion
	delete node;
}

/// Removes specified 'node' from binary search tree, assuming that 
/// it has only one child node.
void remove_1_child_node( Node* node )
{
	// Check the condition
	assert( (node->_left != nullptr) ^ (node->_right != nullptr) );
	// Remember adjacent nodes
	const bool has_right = (node->_right != nullptr);
	Node* p = node->_parent;
	Node* c = ( has_right ? node->_right : node->_left );
	// Obtain pointer to the pointer, which points to 'node' from its 
	// parent node.
	Node** parent_ptr_ptr = nullptr;
	if ( p != nullptr ) {
		if ( node == p->_left ) {
			// 'p' points to 'node' by its '_left' pointer.
			parent_ptr_ptr = &( p->_left );
		}
		else {
			// 'p' points to 'node' by its '_right' pointer.
			parent_ptr_ptr = &( p->_right );
		}
	}
	// Unlink 'node' from the tree and delete it
	if ( has_right )
		node->_right = nullptr;
	else
		node->_left = nullptr;
	delete node;
	// Link parent ('p') and the child ('c') nodes together
	c->_parent = p;
	if ( p )
		*parent_ptr_ptr = c;
}

/// Removes specified 'node' from binary search tree, expecting that 
/// it has 2 child nodes.
void remove_2_child_node( Node* node )
{
	// Check the condition
	assert( (node->_left != nullptr) && (node->_right != nullptr) );
	// Find the replacement node
	Node* replace_node = minimum_recursive( node->_right );
	// Swap their values
	std::swap( node->_value, replace_node->_value );
	// Remove the replacement node instead
	if ( replace_node->_right != nullptr )
		remove_1_child_node( replace_node );
	else
		remove_leaf( replace_node );
}

/// Removes specified 'node' from its binary search tree. The 'node' 
/// argument can have any number of child nodes.
void remove_node( Node* node )
{
	// Delegate, based on presence of child subtrees
	if ( node->_left == nullptr ) {
		if ( node->_right == nullptr )
			remove_leaf( node );
		else
			remove_1_child_node( node );
	}
	else {
		if ( node->_right == nullptr )
			remove_1_child_node( node );
		else
			remove_2_child_node( node );
	}
}
