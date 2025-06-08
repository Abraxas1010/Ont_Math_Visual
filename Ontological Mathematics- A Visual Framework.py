# -*- coding: utf-8 -*-
# %% [markdown]
# # Ontological Mathematics: A Visual Framework
# ### An Apoth3osis R&D Demonstration
#
# **Introduction:**
#
# Welcome to a demonstration of a core concept from the Apoth3osis R&D division. This interactive notebook presents a visual framework for **Ontological Mathematics**, a paradigm that posits reality as fundamentally mathematical and informational.
#
# At Apoth3osis, we believe that the most profound advancements in AI and complex systems modeling will come from a deeper understanding of the universe's foundational rules. This model explores a deterministic, non-random basis for existence, providing a powerful alternative to paradigms reliant on chance or unexplained phenomena.
#
# The following visualization illustrates the core tenets of this theory: the transition from a non-physical, timeless frequency domain (**Pure Being**) to the dynamic, evolving physical world we experience (**Pure Becoming**).

# %% [markdown]
# ## 1. Setup and Dependencies
#
# This notebook requires several Python libraries for numerical operations, graph theory, and animation. The following cell will install a necessary library and then import all dependencies.

# %%
# Install the ipython-canvas library for smoother animations in some environments.
!pip install -q ipython-canvas

# Consolidate all library imports for a clean and organized setup.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

print("Dependencies installed and imported successfully.")


# %% [markdown]
# ## 2. The Core Concept: From Frequency to Spacetime
#
# Ontological Mathematics proposes that the universe originates from **monads**—indivisible, eternal mathematical entities. Each monad is a complete frequency domain, best described by **Euler's formula** ($e^{i\theta} = \cos\theta + i\sin\theta$), which elegantly unifies waves and circles.
#
# Collectively, these monads form an infinite "Hive Mind," a universal frequency domain outside of space and time. The physical world emerges from this domain via the **Ontological Fourier Transform**.
#
# **Why is this useful?** The Fourier Transform is a powerful mathematical tool that decomposes complex patterns into a combination of simple sine and cosine waves. In this context, it acts as the universal "projection" mechanism, translating the timeless, non-physical information of the frequency domain into the structured, evolving reality of spacetime. This provides a causal, deterministic link between the non-physical and the physical.

# %% [markdown]
# ## 3. The Visualization Engine
#
# To make these abstract concepts tangible, we've developed a robust visualization class. This class encapsulates the entire animation logic, ensuring the code is modular, reusable, and well-documented. It handles the creation of the animation stages, the rendering of mathematical concepts, and the final presentation.
#
# This approach avoids security risks associated with data handling by being entirely self-contained; it generates all its data programmatically and requires no external file access.

# %%
class OntologicalVisualizer:
    """
    A class to create and manage the visualization of Ontological Mathematics concepts.

    This class encapsulates the Matplotlib figure, animation logic, and state management
    to provide a clean and robust presentation of the transition from the frequency
    domain to the physical domain of interacting monads.
    """

    def __init__(self, num_monads=10, frames_per_stage=120):
        """
        Initializes the visualizer and its parameters.

        Args:
            num_monads (int): The number of monads to represent in the Hive Mind.
                              This is a finite representation of an infinite concept.
            frames_per_stage (int): The number of animation frames for each conceptual stage.
                                    Higher values result in a slower, smoother animation.
        """
        self.num_monads = num_monads
        self.frames_per_stage = frames_per_stage
        self.total_frames = 5 * frames_per_stage  # There are 5 distinct stages

        # --- Setup the plotting environment ---
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.fig.patch.set_facecolor('white')
        self.ax.set_facecolor('white')

        # --- Initialize graph for the Hive Mind ---
        # The NetworkX graph represents the collection of monads.
        self.G = nx.Graph()
        self.G.add_nodes_from(range(self.num_monads))
        # The spring layout provides a visually pleasing distribution of nodes.
        self.pos = nx.spring_layout(self.G, seed=42)

        # Add edges for a connected visualization in the final stage
        for i in range(self.num_monads):
            self.G.add_edge(i, (i + 1) % self.num_monads)


    def _animate(self, frame):
        """The main animation loop called by FuncAnimation."""
        self.ax.clear()
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        # Determine the current stage and frame within that stage
        stage = frame // self.frames_per_stage
        stage_frame = frame % self.frames_per_stage
        
        # Use a try-except block for robust handling of animation stages
        try:
            if stage == 0:
                self._draw_frequency_domain(stage_frame)
            elif stage == 1:
                self._transition_to_singularity(stage_frame)
            elif stage == 2:
                self._emerge_hive_mind(stage_frame)
            elif stage == 3:
                self._draw_monadic_interactions(stage_frame)
            elif stage == 4:
                self._draw_physical_domain(stage_frame)
        except Exception as e:
            print(f"An error occurred during animation at frame {frame}: {e}")
            # Optionally, stop the animation
            self.ani.event_source.stop()


    def _draw_frequency_domain(self, frame):
        """Stage 1: Visualize the infinite frequency domain (Pure Being)."""
        alpha = max(0, 1 - (frame / self.frames_per_stage))
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        infinity = plt.Circle((0, 0), 0.7, fill=False, color='black', alpha=alpha)
        self.ax.add_artist(infinity)
        self.ax.text(0, 0, r'$\infty$', fontsize=40, ha='center', va='center', alpha=alpha)
        self.ax.set_title("Stage 1: The Infinite Frequency Domain (Pure Being)", alpha=alpha)


    def _transition_to_singularity(self, frame):
        """Stage 2: The domain collapses into a singularity."""
        scale = max(0, 1 - (frame / self.frames_per_stage))
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.plot(0, 0, 'ro', markersize=10 * (1 - scale))
        alpha = 1 - scale
        self.ax.set_title("Stage 2: The Singularity - The Point of Origin", alpha=alpha)


    def _emerge_hive_mind(self, frame):
        """Stage 3: The Hive Mind of monads emerges from the singularity."""
        progress = frame / self.frames_per_stage
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)

        # Nodes move from the center to their final positions
        current_pos = {node: pos * progress for node, pos in self.pos.items()}
        nx.draw_networkx_nodes(self.G, current_pos, ax=self.ax, node_size=200, node_color='red')
        self.ax.set_title("Stage 3: Emergence of the Monadic Hive Mind", alpha=progress)


    def _draw_monadic_interactions(self, frame):
        """Stage 4: Each monad shown as a self-contained frequency domain (Euler's formula)."""
        progress = frame / self.frames_per_stage
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)
        
        # Center the nodes to focus on their internal nature
        pos_center = {i: (0, 0) for i in self.G.nodes()}
        nx.draw_networkx_nodes(self.G, pos_center, ax=self.ax, node_size=200, node_color='red', alpha=progress)

        # Draw concentric circles representing monadic frequencies
        for i in range(1, 6):
            circle = plt.Circle((0, 0), i * 0.2, fill=False, alpha=progress)
            self.ax.add_artist(circle)
            angle = progress * 2 * np.pi
            x, y = i * 0.2 * np.cos(angle), i * 0.2 * np.sin(angle)
            self.ax.plot(x, y, 'bo', markersize=5, alpha=progress)
        
        self.ax.set_title("Stage 4: Monads as Individual Frequency Domains", alpha=progress)


    def _draw_physical_domain(self, frame):
        """Stage 5: The physical domain (Pure Becoming) with wave-based interactions."""
        progress = frame / self.frames_per_stage
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.set_title("Stage 5: The Physical Domain (Pure Becoming)", alpha=progress)

        # Draw the full graph
        nx.draw_networkx_nodes(self.G, self.pos, ax=self.ax, node_size=200, node_color='red', alpha=progress)
        nx.draw_networkx_edges(self.G, self.pos, ax=self.ax, alpha=0.3 * progress)

        # Animate waves along the edges, representing Fourier-based communication
        angle = frame * np.pi / 50
        for i, j in self.G.edges():
            xi, yi = self.pos[i]
            xj, yj = self.pos[j]
            dx, dy = xj - xi, yj - yi
            dist = np.sqrt(dx**2 + dy**2)
            
            wave_t = np.linspace(0, 1, 50)
            wave_x = xi + wave_t * dx
            wave_y = yi + wave_t * dy
            
            # Perpendicular offset for wave visualization
            sine_offset = 0.05 * np.sin(2 * np.pi * wave_t * 4 - angle)
            
            # Draw sine wave along the edge path
            self.ax.plot(wave_x - sine_offset * dy/dist, 
                         wave_y + sine_offset * dx/dist, 
                         'b-', linewidth=1.0, alpha=progress)


    def run_animation(self):
        """Creates and runs the complete animation."""
        # Use a class attribute for the animation object to prevent it from being garbage-collected.
        self.ani = FuncAnimation(
            self.fig, 
            self._animate, 
            frames=self.total_frames, 
            interval=50,  # Interval in milliseconds
            repeat=False
        )
        plt.tight_layout()
        plt.show()


# %% [markdown]
# ## 4. Running the Demonstration
#
# The code cell below will now create an instance of our `OntologicalVisualizer` and run the animation. Observe the five distinct stages as they unfold:
#
# 1.  **The Infinite Frequency Domain:** A representation of all potentiality, existing outside space and time.
# 2.  **The Singularity:** The collapse of potentiality into a single, unified point of origin.
# 3.  **Emergence of the Hive Mind:** The singularity gives rise to a network of individual monads.
# 4.  **Monadic Interactions:** A look inside the monadic system, showing how each entity is a source of frequencies (waves).
# 5.  **The Physical Domain:** The complete system, where monads interact via the exchange of wave information to create the fabric of physical reality.

# %%
if __name__ == '__main__':
    # Instantiate and run the visualization
    visualizer = OntologicalVisualizer(num_monads=12, frames_per_stage=150)
    visualizer.run_animation()

# %% [markdown]
# ## 5. Conclusion and Key Takeaways for the Client
#
# This visualization provides a concrete, intuitive model for what is typically a highly abstract concept. The key takeaways from this demonstration are:
#
# * **A Deterministic Universe:** Ontological Mathematics provides a framework for a universe founded on reason and mathematical law, not randomness or uncaused events. This aligns with our mission at Apoth3osis to build robust, predictable AI systems.
#
# * **The Power of Frequency:** By defining the universe in terms of frequencies, we can use powerful, time-tested tools like the Fourier Transform to understand and model complex systems. This has direct applications in signal processing, pattern recognition, and building more sophisticated AI models of the world.
#
# * **Bridging a Foundational Gap:** This approach directly addresses the "hard problem" of how a non-physical reality (like information or consciousness) can give rise to a physical one. By demonstrating a clear mathematical bridge, it opens new avenues for research in both physics and artificial intelligence.
#
# We believe this line of R&D is crucial for developing next-generation AI that doesn't just learn from data, but understands the fundamental principles of the system in which it operates.