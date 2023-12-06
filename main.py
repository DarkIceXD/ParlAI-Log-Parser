
import matplotlib.pyplot as plt
import parlai_log_parser


def main():
    data = parlai_log_parser.parse('log.txt')
    fig, ax = plt.subplots()

    ax.plot(data['epochs'], data['blended_skill_talk']
            ['loss'], label='blended_skill_talk')
    ax.plot(data['epochs'], data['convai2:normalized']
            ['loss'], label='convai2:normalized')
    ax.plot(data['epochs'], data['wizard_of_wikipedia']
            ['loss'], label='wizard_of_wikipedia')

    ax.set_xlabel('Epochs')
    ax.set_ylabel('Loss')

    ax.legend()

    fig.savefig('plot.png')


if __name__ == '__main__':
    main()
