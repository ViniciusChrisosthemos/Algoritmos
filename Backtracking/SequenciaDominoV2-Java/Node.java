
public class Node {
	int left;
	int right;
	boolean marked;
	
	public Node(int left, int right) {
		this.left = left;
		this.right = right;
		this.marked = false;
	}
	
	@Override
	public String toString() {
		return "(" + left + ","+ right + ")";
	}
}
