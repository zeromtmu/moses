import argparse


def get_parser():
    parser = argparse.ArgumentParser()

    model_arg = parser.add_argument_group('Model')
    model_arg.add_argument('--embedding_size', type=int, default=32,
                           help='Embedding size in encoder and decoder')
    model_arg.add_argument('--encoder_hidden_size', type=int, default=380,
                           help='Size of hidden state for lstm layers in encoder')
    model_arg.add_argument('--encoder_num_layers', type=int, default=1,
                           help='Number of lstm layers in encoder')
    model_arg.add_argument('--encoder_bidirectional', type=bool, default=True,
                           help='If true to use bidirectional lstm layers in encoder')
    model_arg.add_argument('--encoder_dropout', type=float, default=0,
                           help='Dropout probability for lstm layers in encoder')
    model_arg.add_argument('--decoder_hidden_size', type=int, default=640,
                           help='Size of hidden state for lstm layers in decoder')
    model_arg.add_argument('--decoder_num_layers', type=int, default=2,
                           help='Number of lstm layers in decoder')
    model_arg.add_argument('--decoder_dropout', type=float, default=0,
                           help='Dropout probability for lstm layers in decoder')
    model_arg.add_argument('--latent_size', type=int, default=640,
                           help='Size of latent vectors')
    model_arg.add_argument('--discriminator_layers', nargs='+', type=int, default=[640, 256],
                           help='Numbers of features for linear layers in discriminator')

    train_arg = parser.add_argument_group('Training')
    train_arg.add_argument('--pretrain_epochs', type=int, default=0,
                           help='Number of epochs for autoencoder pretraining')
    train_arg.add_argument('--train_epochs', type=int, default=25,
                           help='Number of epochs for autoencoder training')
    train_arg.add_argument('--n_batch', type=int, default=128,
                           help='Size of batch')
    train_arg.add_argument('--lr', type=float, default=1e-3,
                           help='Learning rate')
    train_arg.add_argument('--n_jobs', type=int, default=1,
                           help='Number of threads')

    return parser


def get_config():
    parser = get_parser()
    return parser.parse_known_args()[0]
