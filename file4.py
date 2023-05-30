import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def create_animation():
    # Create figure and axis
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Initialize line plot
    line, = ax.plot(x, y)

    # Set axis labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sine Wave Animation')

    # Animation update function
    def update(frame):
        line.set_ydata(np.sin(x + frame/10))
        return line,

    # Create animation
    ani = plt.FuncAnimation(fig, update, frames=100, interval=100)

    return ani

def main():
    st.title("Simple Animation with Matplotlib")
    st.write("This app creates a simple animation using Matplotlib.")

    ani = create_animation()

    # Display animation using Streamlit
    st.pyplot(ani._fig, use_container_width=True)

if __name__ == "__main__":
    main()
