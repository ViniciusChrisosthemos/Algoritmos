import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class App {
	
	public List<Node> findPath(List<Node> nodes){
		Node node = nodes.get(0);
		node.marked = true;
		List<Node> startPath = new LinkedList<>();
		startPath.add(node);
		return findPath(nodes, node.left, node.right, startPath);
	}
	
	private List<Node> findPath(List<Node> nodes, int left, int right, List<Node> path){
		boolean last = true;
		for (Node node : nodes) {
			if (node.marked) continue;
			
			last = false;
			
			if (node.left == left) {
				node.marked = true;
				path.add(0,node);
				List<Node> fpath = findPath(nodes, node.right, right, path);
				if (!fpath.isEmpty()) return path;
				node.marked = false;
				path.remove(0);
			}
			
			if (node.right == left) {
				node.marked = true;
				path.add(0,node);
				List<Node> fpath = findPath(nodes, node.left, right, path);
				if (!fpath.isEmpty()) return path;
				node.marked = false;
				path.remove(0);
			}
			
			if (node.left == right) {
				node.marked = true;
				path.add(node);
				List<Node> fpath = findPath(nodes, left, node.right, path);
				if (!fpath.isEmpty()) return path;
				node.marked = false;
				path.remove(path.size()-1);
			}
			
			if (node.right == right) {
				node.marked = true;
				path.add(node);
				List<Node> fpath = findPath(nodes, left, node.left, path);
				if (!fpath.isEmpty()) return path;
				node.marked = false;
				path.remove(path.size()-1);
			}
		}
		
		if (last) return path;
		return new LinkedList<>();
	}
	
	public static void main(String[] args) {
		 List<Node> nodes = new LinkedList<>();
		 nodes.add(new Node(4,2));
		 nodes.add(new Node(3,4));
		 nodes.add(new Node(8,1));
		 nodes.add(new Node(1,7));
		 nodes.add(new Node(4,7));
		 nodes.add(new Node(2,8));
		 
		 Collections.shuffle(nodes);
		 System.out.println(nodes);
		 System.out.println((new App()).findPath(nodes));
	}
}
